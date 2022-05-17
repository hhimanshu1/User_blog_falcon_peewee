import falcon
from api.middlewares import (PeeweeConnectionMiddleware,AuthorizationMiddleware)

app=falcon.API(middleware=[PeeweeConnectionMiddleware()])

import api.routes