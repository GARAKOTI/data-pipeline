import os
from kafka import KafkaProducer
import requests
import json
import time

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
KAFKA_TOPIC = "random_users"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def fetch_random_user():
    response = requests.get("https://randomuser.me/api/")
    data = response.json()
    return data['results'][0]

def produce():
    while True:
        user_data = fetch_random_user()
        print(f"Sending user: {user_data}")
        producer.send(KAFKA_TOPIC, value=user_data)
        time.sleep(60)

if __name__ == "__main__":
    produce()
