import os
from mongoengine import Document, StringField, BooleanField, connect
from dotenv import load_dotenv

load_dotenv()

USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')

connect(db='hw', host=f'mongodb+srv://{USER_NAME}:{PASSWORD}@cluster0.q1gz4ma.mongodb.net/')

class Contact(Document):
    full_name = StringField(required=True, max_length=100)
    email = StringField(required=True, unique=True)
    sent = BooleanField(default=False)
    additional_info = StringField()