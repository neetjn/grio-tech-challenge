from r2dto import Serializer, fields


class Link(object):
    def __init__(self, rel=None, href=None):
        self.rel = rel
        self.href = href


class LinkSerializer(Serializer):
    rel = fields.StringField()
    href = fields.StringField()

    class Meta(object):
        model = Link


class User(object):
    def __init__(self):
        self.href = ''
        self.links = []
        self.name = ''
        self.line1 = ''
        self.line2 = ''
        self.city = ''
        self.state = ''
        self.zip = ''
        self.phone = ''


class UserSerializer(Serializer):
    href = fields.StringField()
    links = fields.ListField(fields.ObjectField(LinkSerializer))

    class Meta(object):
        model = User
