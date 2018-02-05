import datetime

from grio.db import client, Person, Address
from grio.errors import PersonNotFoundError
from grio.mediatypes import PersonDto, PeopleDto


def person_to_dto(person):
    """
    Serialize `Person` instance to data transfer object.

    :param person: Instance to convert.
    :type person: Person
    :returns: PersonDto
    """
    primary_address = Address.get_by_id(person.primary_address)
    try:
        secondary_address = Address.get_by_id(person.secondary_address)
    except Address.DoesNotExist:
        secondary_address = None
    return PersonDto(
        name=person.name,
        line1=primary_address.address_line,
        line2=secondary_address.address_line if secondary_address else '',
        city=primary_address.city,
        state=primary_address.state,
        zip_code=primary_address.zip_code,
        phone=person.phone)


def address_from_dto(person_dto):
    """
    Find or creates address resource from provided data transfer object.

    >> (primary_address, secondary_address

    :param person_dto: Data transfer object to convert from.
    :type person_dto: PersonDto
    :returns: tuple
    """
    try:
        primary_address = Address.get(
            Address.address_line == person_dto.line1,
            Address.city == person_dto.city,
            Address.state == person_dto.state,
            Address.zip_code == person_dto.zip_code)
    except Address.DoesNotExist:
        primary_address = Address.create(
            address_line=person_dto.line1,
            city=person_dto.city,
            state=person_dto.state,
            zip_code=person_dto.zip_code)
    if person_dto.line2:
        try:
            secondary_address = Address.get(
                Address.address_line == person_dto.line2,
                Address.city == person_dto.city,
                Address.state == person_dto.state,
                Address.zip_code == person_dto.zip_code)
        except Address.DoesNotExist:
            secondary_address = Address.create(
                address_line=person_dto.line2,
                city=person_dto.city,
                state=person_dto.state,
                zip_code=person_dto.zip_code)
    else:
        secondary_address = None

    return (primary_address, secondary_address)


def get_people(query=None):
    """
    Finds people by search criteria.

    :param query: Content to query for.
    :type query: string
    :returns: [PeopleDto, (...id)]
    """

    if query:
        people = (Person.select()
            .join(Address, on=(Person.primary_address == Address.address_id))
            .where(
                Person.is_deleted == False,
                (Person.name.contains(query)) | (Person.phone.contains(query)) |
                (Address.address_line.contains(query)) | (Address.zip_code.contains(query)) |
                (Address.state.contains(query)) | (Address.state.contains(query))))
    else:
        people = (Person.select().where(Person.is_deleted == False))

    result = [PeopleDto(), []]
    people_dto, ids = result
    for person in people:
        people_dto.people.append(person_to_dto(person))
        ids.append(person.id)
    return result

def create_person(person_dto):
    """
    Create a new user from provided data transfer object.

    :param person_dto: Data transfer object to convert from.
    :type person_dto: PersonDto
    :returns: (PersonDto, id)
    """

    # TODO: implement duplicate check -- need another unique identifier for people

    primary_address, secondary_address = address_from_dto(person_dto)
    person = Person.create(
        name=person_dto.name,
        phone=person_dto.phone,
        primary_address=primary_address.address_id,
        secondary_address=secondary_address.address_id if secondary_address else None)

    return (person_to_dto(person), person.id)

def get_person(person_id):
    """
    Return person data transfer object from provided primary key.

    :param person_id: Primary key to search by.
    :type person_id: string
    :returns: PersonDto
    """
    person = Person.get_by_id(person_id)
    if person.deleted:
        raise PersonNotFoundError()
    return person_to_dto(person)


def delete_person(person_id):
    """
    Delete person by provided unique key.

    :param person_id: Primary key to search by.
    :type person_id: string
    :returns: None
    """
    person = Person.get_by_id(person_id)
    if person.deleted:
        raise PersonNotFoundError()
    person.is_deleted = True
    person.deleted = datetime.datetime.utcnow
    person.save()


def update_person(person_id, person_dto):
    """
    Update person by provided unique key.

    :param person_id: Primary key to search by.
    :type person_id: string
    :param person_dto: Data transfer object to merge data from.
    :type person_dto: PersonDto
    :returns: None
    """
    person = Person.get_by_id(person_id)
    if person.deleted:
        raise PersonNotFoundError()

    primary_address, secondary_address = address_from_dto(person_dto)

    person.name = person_dto.name
    person.primary_address = primary_address.address_id
    person.secondary_address = secondary_address.address_id if secondary_address else None
    person.phone = person_dto.phone
    person.save()
