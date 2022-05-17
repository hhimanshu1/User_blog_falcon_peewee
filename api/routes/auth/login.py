import json
from api import app 
from api.models import Credential as Creds
from werkzeug.security import check_password_hash as cph

class LoginResource:
    def on_post(self,req,resp):
        _creds=json.loads(req.stream.read())
        record=Creds.get_or_none(Creds.username==_creds['username'])

        if record:
            if cph(record.hash,_creds['password']):
                resp.body=json.dumps({
                    'status':'pass',
                    'user_id':record.user_id,
                    'user_name':record.name
                })
            else:
                resp.body=json.dumps({
                    'status':'fail',
                    'msg':'Incorrect Password'
                })
        else:
            resp.body=json.dumps({
                'status':'fail',
                'msg':'Username not found'
            })
app.add_route('/login',LoginResource())