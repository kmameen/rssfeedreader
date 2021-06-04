from flask import Flask, jsonify, request
import feedparser
from utils.utils import read_flask_request_body
from utils.web import json_response



app = Flask(__name__)


@app.route('/')
def index():
    return json_response("Hello World")



@app.route("/parse", methods=['POST'])
def parser():
    body = read_flask_request_body()

    if body is None or body.get('url', None) is None:
        return "URL isn't passed"
    
    url = body.get('url')
    feed = feedparser.parse(url)
    result = []
    for entry in feed.entries:
        result.append(entry.link)

    return jsonify({'result': result})
    




if __name__ == '__main__':
    app.debug = True
    app.run()