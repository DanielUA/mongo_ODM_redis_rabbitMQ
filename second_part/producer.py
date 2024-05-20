import os
import json
import pika
from faker import Faker
from models import Contact
from dotenv import load_dotenv

fake = Faker()

load_dotenv()

def create_fake_contacts(n):
    contacts = []
    for _ in range(n):
        contact = Contact(
            full_name=fake.name(),
            email=fake.email(),
            additional_info=fake.address()
        )
        contact.save()
        contacts.append(contact)
    return contacts

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='email_queue', durable=True)

    contacts = create_fake_contacts(10)
    
    for contact in contacts:
        message = json.dumps({'id': str(contact.id)})
        channel.basic_publish(
            exchange='',
            routing_key='email_queue',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))
        print(f" [x] Sent {message}")

    connection.close()

if __name__ == "__main__":
    main()
