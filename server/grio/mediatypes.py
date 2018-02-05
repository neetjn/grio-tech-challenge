from r2dto import Serializer, fields


class LinkDto(object):
    def __init__(self, rel=None, href=None):
        self.rel = rel
        self.href = href


class LinkDtoSerializer(Serializer):
    rel = fields.StringField()
    href = fields.StringField()

    class Meta(object):
        model = LinkDto


class PersonDto(object):
    def __init__(self, name=None, line1=None, line2=None, city=None, state=None, zip_code=None, phone=None):
        self.href = ''
        self.links = []
        self.name = name
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone


class PersonDtoSerializer(Serializer):
    href = fields.StringField()
    links = fields.ListField(fields.ObjectField(LinkDtoSerializer))
    name = fields.StringField()
    line1 = fields.StringField()
    line2 = fields.StringField()
    city = fields.StringField()
    state = fields.StringField()
    zip_code = fields.StringField(name="zip")
    phone = fields.StringField()

    class Meta(object):
        model = PersonDto


class PeopleDto(object):
    def __init__(self, people=None):
        self.people = people or []


class PeopleDtoSerializer(Serializer):
    people = fields.ListField(fields.ObjectField(PersonDtoSerializer))

    class Meta(object):
        model = PeopleDto
