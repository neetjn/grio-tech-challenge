from peewee import *
from constants import *


client = PostgresqlDatabase(DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT) \
    if DB_USER else PostgresqlDatabase(DB_NAME, host=DB_HOST, port=DB_PORT)


class Address(Model):
    address_id = PrimaryKeyField()
    address_line = TextField(unique=True, null=False)
    state = CharField(null=False)
    zip_code = CharField(null=False)


class Person(Model):
    user_id = PrimaryKeyField()
    name = CharField(null=False)
    phone = TextField(null=False)
    primary_address = ForeignKeyField(Address, to_field='address_id')
    secondary_address = ForeignKeyField(Address, to_field='address_id')


def bootstrap(self):



def drop_database(self):
    client.drop_tables([User])
