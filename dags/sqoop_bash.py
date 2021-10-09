
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

class SqoopReturn(BashOperator):
    #def __init__(self, bash_command, **kwargs,) -> None:
        #super().__init__(self, bash_command, **kwargs,)

    def execute():
        super().execute()
        print('##########', result.exit_code)
        xcom_push(key='sq_bash', value=result.exit_code)





args = {
    'owner': 'airflow',
}

dag=DAG(
    dag_id='sqoop_import',
    default_args=args,
    schedule_interval='*/2 * * * *',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
    tags=['sqoop', 'import'],
)

sqoop_imp = SqoopReturn(
        task_id='sqoop_import',
        bash_command='sqoop import --connect jdbc:mysql://localhost/test --username hduser_ --password pass1212 --table test --m 1 --target-dir /test',
        dag=dag,
        )

ls_hdfs = BashOperator(
        task_id='hdfs_ls',
        bash_command='hadoop fs -ls /test',
        dag=dag,
        )

sqoop_imp >> ls_hdfs


if __name__ == "__main__":
    dag.cli()
