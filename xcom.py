
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from random import randrange
from datetime import datetime

default_args = {
'start_date': datetime(2021, 9, 7)
}

def _training_model(ti):
    ac = randrange(0.1, 1)
    print('model accuracy: {accuracy}')
    
    #this will directly write to xcom as key=return, value=ac(value), "task_id"
    #return ac 
    #else we can also do by using ti-> task instance
    #ti.xcom_push(key='whatever key we want', value='value')
    ti.xcom_push(key='accu', value=ac)

def _choose_best_model(ti):
    #return the xcom value by ti.xcom_pull(key='',task_ids='')
    tsk = m_A
    accu_o = [0.1,0.3,0.5,0.7,0.9]
    accu_e = [0.2,0.4,0.6,0.8,1]

    ac = ti.xcom_pull(key='accu', task_ids=tsk)
    print(' model A', ret)
    if ac in accu_o:
	return 'even_ts'
    elif ac in accu_e:
	return 'odd_ts'
    else:
	return 'error_ts'


with DAG('xcom_dag', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    downloading_data = BashOperator(
		    task_id='downloading_data',
		    bash_command='sleep 3'
		    do_xcom_push = False
		    )

    training_model_task = [PythonOperator(
			    task_id= 'm_{task}',
			    python_callable=_training_model
			) for task in ['A', 'B', 'C']]

    choose_model = BranchPythonOperator(
		    task_id='choose_model',
		    python_callable=_choose_best_model
		)
    even_ts = PythonOperator(
		task_id = 'even_ts'
		python_callable = _even_ts
	    )

    odd_ts = PythonOperator(
		task_id = 'odd_ts'
		python_callable = _odd_ts
	    )
    
    error_ts = PythonOperator(
		task_id = 'error_ts'
		python_callable = _error_ts
	    )

downloading_data >> training_model_task >> choose_model
choose_model >> [even_ts, odd_ts, error_ts]
