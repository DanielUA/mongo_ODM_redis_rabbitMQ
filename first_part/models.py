import os

from dotenv import load_dotenv
from mongoengine import connect, Document, StringField, ReferenceField, ListField, CASCADE

load_dotenv()

USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')

connect(db='hw', host=f'mongodb+srv://{USER_NAME}:{PASSWORD}@cluster0.q1gz4ma.mongodb.net/')

class Author(Document):
    fullname = StringField(required = True, unique=True)
    born_date = StringField(max_length=150)
    born_location = StringField(max_length=150)
    description = StringField()
    meta = {'collections': 'authors'}

class Quote(Document):
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=20))
    quote = StringField()
    meta = {'collections': 'qoutes'}
