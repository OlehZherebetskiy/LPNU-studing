from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField





class User(Document):
    name = StringField(max_length=60, required=True, unique=True)
    password = StringField(max_length=60, required=True, unique=True)
    moderator = StringField(max_length=60, required=True, unique=True)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Article(Document):
    name = StringField(max_length=60, required=True, unique=False)
    title = StringField(max_length=60, required=True, unique=True)
    text = StringField(max_length=10000, required=True, unique=False)
    requester = StringField(max_length=60, required=True, unique=False)
    patron_id = StringField(max_length=60, required=True, unique=False)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name