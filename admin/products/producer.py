import os
import json
import pika
from dotenv import main

main.load_dotenv()

params = pika.URLParameters(os.environ.get("AMQP_URL"))
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='main')


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
