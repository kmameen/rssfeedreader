import json
from flask import request




def read_flask_request_body():
    if request.data:
        return json.loads(request.data)

    return None