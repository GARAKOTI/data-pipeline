FROM bitnami/spark:3.4

USER root

# Install Kafka dependency for Spark Structured Streaming
RUN mkdir -p /opt/spark/jars && \
    curl -o /opt/spark/jars/spark-sql-kafka-0-10_2.12-3.4.1.jar https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.4.1/spark-sql-kafka-0-10_2.12-3.4.1.jar && \
    curl -o /opt/spark/jars/kafka-clients-3.4.0.jar https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.4.0/kafka-clients-3.4.0.jar

COPY scripts /opt/spark-apps

WORKDIR /opt/spark-apps

CMD ["sleep", "infinity"]
