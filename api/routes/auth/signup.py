from api import app 
import json
from api.models import Credential as Creds 
from werkzeug.security import generate_password_hash as gph

class SignupResource:
    def on_post(self,req,resp):
        _info=json.loads(req.stream.read())
        if Creds.select().where(Creds.username==_info['username']).exists():
            resp.body=json.dumps({
                'status':'fail',
                'msg':'Username Already Taken'
            })

        else:
            Creds.create(
                username=_info['username'],
                hash=gph(_info['password']),
                email=_info['email'],
                name=_info['name'],
            )
            ins_id=Creds.select().order_by(Creds.user_id.desc()).get()
            resp.body=json.dumps({
                'status':'pass',
                'user_id':ins_id.user_id
            })

app.add_route('/signup',SignupResource())