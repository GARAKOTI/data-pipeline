set -euo pipefail

# 1. Variables
ROOT_DIR="$(pwd)"

# 2. Directories
mkdir -p \
  configs/{spark,kafka,airflow,postgres} \
  spark/{eventlogs,jobs,scripts} \
  kafka/producers \
  airflow/{dags,plugins,scripts} \
  postgres/data \
  scripts logs docs

# 3. Placeholder files
touch \
  docker-compose.yml \
  README.md \
  configs/spark/{spark-defaults.conf,spark-env.sh} \
  configs/kafka/server.properties \
  configs/airflow/{airflow.cfg,webserver_config.py} \
  configs/postgres/init.sql \
  spark/jobs/{wordcount.py,kafkastreaming.py} \
  spark/scripts/submit-spark-job.sh \
  kafka/topics.sh \
  kafka/producers/producer.py \
  airflow/dags/spark_pipeline_dag.py \
  airflow/scripts/trigger_kafka_producer.sh \
  scripts/{build-images.sh,teardown.sh} \
  docs/architecture.md

echo "✅ Scaffold complete at $ROOT_DIR"
