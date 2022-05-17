from api.middlewares import db 
import datetime
from peewee import *

class BaseModel(Model):
    class Meta:
        database=db

class Credential(BaseModel):
    user_id=AutoField()
    username=CharField()
    hash=CharField()
    email=CharField()
    name=CharField()

    class Meta:
        db_table='credentials'

class Posts(BaseModel):
    post_id=AutoField()
    author_uid=CharField()
    post_url=CharField()
    title=CharField()
    body=TextField()
    preview_text=CharField()
    likes=IntegerField(default=0)
    time=DateField(default=datetime.datetime.now)

    class Meta:
        db_table='posts'

class Comments(BaseModel):
    comment_id=AutoField()
    autho_uid=IntegerField()
    post_uid=IntegerField()
    body=TextField()
    time=DateField(default=datetime.datetime.now)

    class Meta:
        db_table='comments'

# db.create_tables([Credential,Posts,Comments])