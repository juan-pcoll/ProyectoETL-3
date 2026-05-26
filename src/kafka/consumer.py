import json
import pandas as pd
from kafka import KafkaConsumer
from sqlalchemy import create_engine


# PostgreSQL connection
engine = create_engine(
    'postgresql://airflow:airflow@postgres:5432/ods_pobreza'
)

# Kafka consumer con timeout para no bloquear el DAG indefinidamente
consumer = KafkaConsumer(
    'personas_metrics',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    consumer_timeout_ms=10000,  # termina si no llegan mensajes en 10 segundos
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Consumer listening...\n")

messages_processed = 0

for message in consumer:

    data = message.value

    print(f"Received: {data}")

    df = pd.DataFrame([data])

    df.to_sql(
        'personas_metrics_log',  # nombre corregido, coherente con el dominio
        engine,
        if_exists='append',
        index=False
    )

    messages_processed += 1
    print(f"Saved to PostgreSQL\n")

print(f"Consumer finished. Messages processed: {messages_processed}")