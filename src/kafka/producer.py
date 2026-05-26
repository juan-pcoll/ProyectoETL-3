import json
import pandas as pd

from kafka import KafkaProducer
from sqlalchemy import create_engine

TOPIC = "personas_metrics"

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

engine = create_engine(
    "postgresql://airflow:airflow@postgres:5432/ods_pobreza"
)

print("Starting Kafka Producer...\n")

query = """
SELECT COUNT(*) AS total_personas
FROM fact_persona
"""

df = pd.read_sql(query, engine)

metric = {
    "total_personas": int(df["total_personas"][0])
}

producer.send(TOPIC, value=metric)

producer.flush()

print(f"Sent: {metric}")