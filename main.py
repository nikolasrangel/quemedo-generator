from flask import Flask
from flask import json
from random import randint

app = Flask(__name__, static_url_path='/static')

como_ousas = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    8: "i",
    9: "j",
    10: "h",
}

def make_json(count, str):
    if(count == 8):
        response = {
            'flag': True,
            'data': "https://www.wikihow.com/Stop-Procrastinating"
        }
    else:
        response = {
            'flag': False,
            'data': str
        }
    return response


@app.route('/')
def static_file():
    return app.send_static_file('index.html')

@app.route("/api/prove/<count>")
def hello_world(count):
    random_value = randint(0, 10)
    json_response = json.dumps(make_json(count, random_value))
    return json_response, 200

app.run()