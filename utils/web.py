from flask import jsonify
from cgi import escape

from werkzeug.wrappers import response



def sanitize(data):
    if isinstance(data, dict):
        for key in list(data.keys()):
            data[key] = sanitize(data[key])
    elif isinstance(data, (list, tuple)):
        for index in range(len(data)):
            data[index] = sanitize(data[index])
    elif isinstance(data, str):
        return escape(data)
    else:
        return data



def json_response(raw_data):

    sanitize(raw_data)

    response = jsonify(raw_data)

    return response
