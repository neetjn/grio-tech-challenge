from peewee import *
import datetime

psql_db = PostgresqlDatabase('my_database', user='postgres')

class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = psql_db

class User(BaseModel):
    username = CharField()

