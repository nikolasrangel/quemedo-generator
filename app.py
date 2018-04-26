from flask import Flask
from flask import json
from flask_cors import CORS
from random import randint

app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
cors = CORS(app, resources={r"/*": {"origins": "*"}})

como_ousas = {
    0: "Entra, suposto filho do capeta!",
    1: "Eu o desafiei. Ele aceitaste meu desafio.",
    2: "Está aqui e agora vou desmacará-lo.",
    3: "Eu vois te provar. Eu vois te provar que sou o filho do capeta.",
    4: "Não é prova porque tu não querdes.",
    5: "Eu vois te provar, eu vou sim.",
    6: "Eu vim das mais profundezas do inferno, de onde tu nunca imagina que eu tenha vindo.",
    7: "Eu vins trazer a desgraça, eu vins trazer os mal, trazer as coisas ruins, traze pobrema pros outro.",
    8: "É PRO-BLE-MA.",
    9: "Eu vim botá os filho dos outro na maconha, espalha maconha.",
    10: "Ah, então tu és traficante, né?",
    11: "Eu não sou traficante não, eu ponho os filho dos outro na maconha.",
    12: "Cheira maconha, fumar cocaína, essas coisas caótica.",
    13: "O que eu quero é espalhar a maldade.",
    14: "Aqui está meu dedo. Quebre meu dedo com a força da mente!",
    15: "Não vois quebrar. Não vois te quebrar seu dedo.",
    16: "Eu não preciso te provar nada, eu não preciso te provar, eu sou o filho do capeta e pronto.",
    17: "Tu não é nadas para mim, tu não é nadas. Tu é um zero a esquerda, tu é um velho, um velho de saia.",
    18: "O que eu quero é espalhar a maldade.",
    19: "Aqui está meu dedo. Quebre meu dedo com a força da mente!",
    20: "Não vois quebrar. Não vois quebrar seu dedo.",
}

def make_json(count, index):
    if(count == 8):
        response = {
            'flag': True,
            'data': "https://www.wikihow.com/Stop-Procrastinating"
        }
    else:
        response = {
            'flag': False,
            'data': como_ousas.get(index)
        }
    return response


@app.route('/')
def static_file():
    return app.send_static_file('index.html')

@app.route("/prove/<count>")
def hello_world(count):
    random_value = randint(0, 20)
    json_response = json.dumps(make_json(count, random_value))
    return json_response, 200

if __name__ == '__main__':
    app.run(debug=True)