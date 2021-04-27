from peewee import *
from datetime import datetime


mysql_db = MySQLDatabase('poemkg2', host='localhost', port=3306, user='poem-kg', password='poem-kg')


class PoemKgBase(Model):
    origin = CharField(max_length=20)
    origin_id = IntegerField(null=False, default=-1)
    url = CharField(max_length=200)
    create_at = DateTimeField(null=False, default=datetime.now(), formats="%Y-%m-%d %H:%M:%S")
    update_at = DateTimeField(null=False, default=datetime.now(), formats="%Y-%m-%d %H:%M:%S")

    class Meta:
        database = mysql_db


class Poem(PoemKgBase):
    title = CharField(max_length=200)
    content = TextField()
    pingyin = TextField()
    author_id = IntegerField(null=False, default=-1)
    author = CharField(max_length=20)
    author_url = CharField(max_length=200)
    dynasty = CharField(max_length=10)
    translate = TextField()
    shangxi = CharField(max_length=200)
    topic = CharField(max_length=100)
    book = CharField(max_length=100)


class Author(PoemKgBase):
    name = CharField(max_length=200)
    detail = TextField()
    dynasty = CharField(max_length=10)
    img_url = CharField(max_length=200)


class Topic(PoemKgBase):
    name = CharField(max_length=30)


class Book(PoemKgBase):
    title = CharField(max_length=30)
    author = CharField(max_length=30)
    author_id = IntegerField()
    detail = TextField()
    img_url = CharField(max_length=200)
    chapter = CharField(max_length=255)


class Dynasty(PoemKgBase):
    name = CharField(max_length=10)
    start = IntegerField(null=False, default=0)
    end = IntegerField(null=False, default=0)
    detail = TextField()


class Idiom(PoemKgBase):
    content = CharField(max_length=30)
    pingyin = CharField(max_length=150)
    explain = CharField(max_length=255)
    come_from = CharField(max_length=255)
    example = CharField(max_length=255)


class Mingjv(PoemKgBase):
    content = CharField(max_length=50)
    come_from = CharField(max_length=255)
    come_from_id = IntegerField(null=False, default=-1)
    author = CharField(max_length=20)
    author_id = IntegerField(null=False, default=-1)
