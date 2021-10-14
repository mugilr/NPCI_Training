
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago


def clear_ts(context):
    ex_time = context.get('execution_date')
    print("##################### Callback #################")
    clear_task = BashOperator(
            task_id = 'clear_task',
            bash_command = f'airflow tasks clear -s {ex_time} -u -d -y 1_sqoop_import'
            )
    return clear_task.execute(context=context)

def check(ti):
    val = ti.xcom_pull(key='error', task_ids = '1_sqoop_import')
    
    print('########  Error $$$$ {0}  $$$$$   #######'.format(val))
    if (val.find('FileAlreadyExistsException') !=-1):
        return 'rm_hdfs'
    else:
        return 'sus'





args = {
    'owner': 'airflow',
}

dag=DAG(
    dag_id='1_sqoop_import',
    default_args=args,
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup = False,
    tags=['sqoop', 'import'],
)

sqoop_imp = BashOperator(
        task_id='1_sqoop_import',
        bash_command='sqoop import --connect jdbc:mysql://localhost/test --username hduser_ --password pass1212 --table test --m 1 --target-dir /test',
        dag=dag,
        )

check_er = BranchPythonOperator(
        task_id = 'check_er',
        python_callable = check,
        #depends_on_past = True,
        trigger_rule = 'all_done',
        dag = dag,
        provide_context=True,
        )

rm_hdfs = BashOperator(
        task_id='rm_hdfs',
        bash_command='hadoop fs -rm -r /test',
        on_success_callback = clear_ts,
        dag=dag,
        )

err_ts = BashOperator(
        task_id = 'err_ts',
        bash_command = 'exit 99',
        on_failure_callback = clear_ts,
        )

sus = BashOperator(
        task_id = 'sus',
        bash_command = 'echo \'Good Job MR\'',
        dag = dag,
        )

sqoop_imp >> check_er >> [rm_hdfs, sus] 
#rm_hdfs >> err_ts


