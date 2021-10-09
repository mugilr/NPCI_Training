from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from airflow.utils.edgemodifier import Label
import random
from datetime import datetime

default_args = {
'start_date': datetime(2021, 9, 7)
}

def _training_model(ti):
    ac = random.randint(1, 10)
    print('model accuracy: {accuracy}')
    
    #this will directly write to xcom as key=return, value=ac(value), "task_id"
    #return ac 
    #else we can also do by using ti-> task instance
    #ti.xcom_push(key='whatever key we want', value='value')
    ti.xcom_push(key='accu', value=ac)

def choose_best_model(ti):
    #return the xcom value by ti.xcom_pull(key='',task_ids='')
    tsk = 'm_A'
    accu_o = [1,3,5,7,9]
    accu_e = [2,4,6,8,10]

    ac = ti.xcom_pull(key='accu', task_ids=tsk)
    print(' model A', ac)
    if ac in accu_o:
        return 'even_ts'
    elif ac in accu_e:
        return 'odd_ts'
    else:
        return 'error_ts'

def even_ts():
    print('Even task')

def odd_ts():
    print('odd task')

def error_ts():
    print('Error task')

with DAG(dag_id='xcom_dag', tags=['xcom','branch'], schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    import_data = BashOperator(
		    task_id='import_data',
		    bash_command='sleep 1'
		    #do_xcom_push = False
		    )

    mata_task = [PythonOperator(
		    task_id= 'm_'+str(task),
		    python_callable=_training_model
		) for task in ['A', 'B', 'C']]

    choose_data = BranchPythonOperator(
		    task_id='choose_data',
		    python_callable = choose_best_model
		)
    even_ts = PythonOperator(
		task_id = 'even_ts',
		python_callable = even_ts
	    )

    odd_ts = PythonOperator(
		task_id = 'odd_ts',
		python_callable = odd_ts
	    )
    
    error_ts = PythonOperator(
		task_id = 'error_ts',
		python_callable = error_ts
	    )

import_data >> Label('importing data') >> mata_task >> Label('Find m_A')  >> choose_data
choose_data >> Label('Based on m_A') >>[even_ts, odd_ts, error_ts]
