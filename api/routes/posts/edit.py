from api import app 
import json
from api.models import Posts
from api.models import Credential as Creds
import falcon

class UpdatePostResource:
    def on_put(self,req,resp):
        username=req.params.get('a')
        post_idf=req.params.get('p')
        if username and post_idf:
            try:
                _=(Posts.update(
                    body=req.media.get('body'),
                    title=req.media.get('title'),
                    preview_text=req.media.get('preview_text'),
                    )).where(
                        (Posts.post_url==post_idf)
                    ).execute()

                resp.body=json.dumps({
                    'status':'pass'
                })

            except:
                resp.body=json.dumps({
                    'status':'fail'
                })

        else:
            raise falcon.HTTPBadRequest(description='Insufficient Argument')

app.add_route('/posts/edit',UpdatePostResource())