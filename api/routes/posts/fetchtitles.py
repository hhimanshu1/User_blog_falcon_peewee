from api import app 
from api.models import Posts
from api.models import Credential as Creds
import json

class FetchTitleResource:
    def on_get(self,req,resp,username):
        user=Creds.get_or_none(Creds.username==username)
        if user is not None:
            posts=Posts.select().where(
                Posts.author_uid==user.get_id()
            ).order_by(Posts.post_id.desc()).dicts()

            payload=[]
            for post in posts:
                payload.append({
                    'date':str(post['time']),
                    'title':post['title'],
                    'url':post['post_url']
                })

            resp.body=json.dumps({
                'status':'pass',
                'result':payload
            })

        else:
            resp.body=json.dumps({
                'status':'fail'
            })

app.add_route('/posts/titles/{username}',FetchTitleResource())