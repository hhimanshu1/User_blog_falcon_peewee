
from api import app 
from api.models import Posts
from api.models import Credential as Creds
import json

class FetchPostResource:
    def on_get(self,req,resp,username,idf):
        post=Posts.get_or_none(Posts.post_url==idf)
        if post is not None:
            user=Creds.get_or_none(Creds.user_id==post.author_id)
            if user is not None:
                if user.username==username:
                    resp.body=json.dumps({
                        'status':'pass',
                        'result':{
                            'post_id':post.get_id(),
                            'title':post.title,
                            'body':post.body,
                            'preview_text':post.preview_text,
                            'idf':idf,
                            'date':str(post.time),
                            'author':{
                                'name':user.name,
                                'username':user.username
                            },
                        }
                    })

                else:
                    resp.body=json.dumps({
                        'status':'fail',
                        'msg':'Username in url does not match'
                    })

            else:
                resp.body=json.dumps({
                    'status':'fail',
                    'msg':'Cannot find author of this blog'
                })

        else:
            resp.body=json.dumps({
                'status':'fail',
                'msg':'No Blog Post found'
            })

app.add_route('/posts/{username}/{idf}',FetchPostResource())