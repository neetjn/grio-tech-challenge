from flask import Flask, Response, redirect, request, url_for
from flask_cors import CORS
from flask_responses import json_response

from grio.core import get_people, get_person, create_person, delete_person, update_person
from grio.mediatypes import PersonDtoSerializer, PeopleDtoSerializer, LinkDto


app = Flask(__name__)
CORS(app, resources={r'/api/*': {'origins': '*'}})


def person_dto_links(person_dto, person_id):
    """
    Create resource links for provided data transfer object.

    :param person_dto: Data transfer object to target.
    :type person_dto: PersonDto
    :param person_id: Resource identifier.
    :type person_id: Resource identifier.
    """
    person_dto.href = url_for('get_person_resource', person_id=person_id)
    person_dto.links = [
        LinkDto(rel="update_person", href=url_for('update_person_resource', person_id=person_id)),
        LinkDto(rel="delete_person", href=url_for('delete_person_resource', person_id=person_id))]

def person_dto_payload(person_dto, person_id, status_code=200):
    """
    Construct payload for person dto.

    :param person_dto: Data transfer object to target.
    :type person_dto: PersonDto
    :param person_id: Resource identifier.
    :type person_id: Resource identifier.
    :return: Response
    """
    person_dto_links(person_dto, person_id)
    p = PersonDtoSerializer(object=person_dto)
    p.validate()
    return json_response(p.data, status_code=status_code)


def paginate(data, index=0, page_size=0):
    if page_size:
        return data[index:index + page_size]
    return data


@app.route('/api/rest/v1/people/', methods=['GET'])
def get_people_resource():
    people_dto, ids = get_people(query=request.args.get('query'))
    index = int(request.args.get('start', 0))
    page_size = int(request.args.get('count', 0))
    people_dto.people = paginate(people_dto.people, index, page_size)
    ids = paginate(ids, index, page_size)
    for i, person_id in enumerate(ids):
        person_dto_links(people_dto.people[i], person_id)
    p = PeopleDtoSerializer(object=people_dto)
    p.validate()
    return json_response(p.data, status_code=200)


@app.route('/api/rest/v1/people/', methods=['POST'])
def create_person_resource():
    data = PersonDtoSerializer(data=request.get_json(silent=True))
    data.validate()
    person_dto, person_id = create_person(data.object)
    return person_dto_payload(person_dto, person_id, 201)


@app.route('/api/rest/v1/people/<person_id>', methods=['GET'])
def get_person_resource(person_id):
    return person_dto_payload(get_person(person_id), person_id, 200)


@app.route('/api/rest/v1/people/<person_id>', methods=['PUT'])
def update_person_resource(person_id):
    content = request.get_json(silent=True)
    person_dto = PersonDtoSerializer(data=content)
    person_dto.validate()
    update_person(person_id, person_dto)
    return redirect(url_for('get_person_resource', person_id=person_id))


@app.route('/api/rest/v1/people/<person_id>', methods=['DELETE'])
def delete_person_resource(person_id):
    delete_person(person_id)
    return Response(status=204)
