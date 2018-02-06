from unittest import TestCase
from grio.core import *
from grio.db import drop_database, bootstrap
from grio.mediatypes import PersonDto


class TestPerson(TestCase):

    def setUp(self):
        drop_database()

    def test_service(self):
        """Ensure basic person/people resource endpoints function as expected"""
        self.assertEqual(len(get_people()[0].people), 0)
        person_dto, person_id = create_person(PersonDto(
            name='John Doe',
            line1='00 Foobar Lane',
            line2='',
            city='Foo Town',
            state='Hawaii',
            zip_code='00000',
            phone='000-000-0000'
        ))
        self.assertEqual(len(get_people()[0].people), 1)
        delete_person(person_id)
        self.assertEqual(len(get_people()[0].people), 0)
