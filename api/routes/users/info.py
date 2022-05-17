from pdb import post_mortem
from api import app 
from api.models import Credential as Creds 
from api.models import Posts
import json


class FetchUserInfoResource:
    def on_get(self,req,resp,username):
        user=Creds.get_or_none(Creds.username==username)
        if user is not None:
            posts_by_user=Posts.select().where(
                Posts.author_uid==user.get_id()
            ).dicts()

            resp.body=json.dumps({
                'status':'pass',
                'result':{
                    'user_id':user.get_id(),
                    'username':user.username,
                    'name':user.name,
                    'email':user.email,
                    'stats':{
                        'posts_count':len(posts_by_user)
                    }
                }
            })
        else:
            resp.body=json.dumps({
                'status':'fail'
            })