
import datetime
import airflow
from airflow import DAG
from airflow.providers.apache.sqoop.operators.sqoop import SqoopOperator
from airflow.utils.dates import days_ago

dag_sqoop = DAG(dag_id="SqoopImp",
            schedule_interval="*/5 * * * *",
            start_date=days_ago(1))

sqoop_imp = SqoopOperator(
                        task_id="sqoop_imp",
                        conn_id="sqoop_local",
                        table="test",
                        cmd_type="import",
                        target_dir="/test",
                        num_mappers=1,
                        dag=dag_sqoop,
                        )

sqoop_imp
