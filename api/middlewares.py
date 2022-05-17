import falcon
from peewee import *
db=PostgresqlDatabase('mydb',user='hhimanshu',password='hhimanshu',host='localhost')

 

KEY='secret'

class PeeweeConnectionMiddleware(object):
    def process_request(self,req,resp):
        db.connect()

    def process_response(self,req,resp,resource,req_succeeded):
        if not db.is_closed():
            db.close()

class AuthorizationMiddleware(object):
    def process_request(self,req,resp):
        if not self._load_token_and_validate(req):
            raise falcon.HTTPUnauthorized('No Authorization token found')

    def _load_token_and_validate(self,req):
        print(req)
        if req.get_header('Authorization')==KEY:
            return True
        return False