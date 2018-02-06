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
        _, person_id = create_person(PersonDto(
            name='John Doe',
            line1='00 Foobar Lane',
            line2='',
            city='Foo Town',
            state='Hawaii',
            zip_code='00000',
            phone='000-000-0000'
        ))
        self.assertEqual(len(get_people()[0].people), 1)
        update_args = {
            'name': 'Jane Doe',
            'line1': '01 Foobar Lane',
            'line2': 'Hello Lane',
            'city': 'Asgard',
            'state': 'Valhalla',
            'zip_code': '11111',
            'phone': '111-111-1111'
        }
        update_person(person_id, PersonDto(**update_args))
        person_dto = get_person(person_id)
        for arg, value in update_args.iteritems():
            self.assertEqual(getattr(person_dto, arg), value)
        delete_person(person_id)
        self.assertEqual(len(get_people()[0].people), 0)
