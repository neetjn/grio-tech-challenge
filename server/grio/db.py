import datetime
import json
from peewee import *
from playhouse.postgres_ext import PostgresqlExtDatabase

from constants import DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT


client = PostgresqlExtDatabase(DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
client.connect()


class PostgresModel(Model):

    class Meta(object):
        database = client


class Address(PostgresModel):
    address_id = PrimaryKeyField()
    address_line = TextField()
    city = CharField()
    state = CharField()
    zip_code = CharField()


class Person(PostgresModel):
    id = PrimaryKeyField()
    name = CharField()
    phone = TextField()
    primary_address = ForeignKeyField(Address, to_field='address_id', null=False)
    secondary_address = ForeignKeyField(Address, to_field='address_id', null=True)
    is_deleted = BooleanField(default=False)
    deleted = DateTimeField(default=None, null=True)


def bootstrap(data=None):
    if (not data):
        data = json.loads(open('grio/_users.json').read())
    for person in data:
        try:
            primary_address = Address.get(
                Address.address_line == person['line1'],
                Address.city == person['city'],
                Address.state == person['state'],
                Address.zip_code == person['zip']).address_id
        except Address.DoesNotExist:
            primary_address = Address.create(
                address_line=person['line1'],
                city=person['city'],
                state=person['state'],
                zip_code=person['zip']).address_id
        if(person.get('line2')):
            try:
                secondary_address = Address.get(
                    Address.address_line == person['line2'],
                    Address.city == person['city'],
                    Address.state == person['state'],
                    Address.zip_code == person['zip']).address_id
            except Address.DoesNotExist:
                secondary_address = Address.create(
                    address_line=person['line2'],
                    city=person['city'],
                    state=person['state'],
                    zip_code=person['zip']).address_id
        else:
            secondary_address = None

        Person.insert(
            name=person['name'],
            phone=person['phone'],
            primary_address=primary_address,
            secondary_address=secondary_address)


def drop_database():
    client.drop_tables([Person, Address])
    client.create_tables([Person, Address])
