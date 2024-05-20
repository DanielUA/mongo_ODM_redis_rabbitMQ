import os
import json
import pika
from models import Contact
from mongoengine import connect
from dotenv import load_dotenv

load_dotenv()

USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')

connect(db='hw', host=f'mongodb+srv://{USER_NAME}:{PASSWORD}@cluster0.q1gz4ma.mongodb.net/')

def send_email(contact):
    # Заглушка для отправки email
    print(f"Sending email to {contact.email}")
    # Имитируем отправку email, можно добавить задержку для реальности
    # time.sleep(2)
    contact.sent = True
    contact.save()

def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    contact_id = message['id']
    contact = Contact.objects(id=contact_id).first()
    if contact and not contact.sent:
        send_email(contact)
        print(f" [x] Email sent to {contact.email}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='email_queue', durable=True)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='email_queue', on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()
