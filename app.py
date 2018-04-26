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
    2: "Ele está aqui e agora vou desmacará-lo.",
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
    18: "[Você é] um vida torta. Um vida torta se fazendo de capetinha! Um lunático.",
    19: "Tu tá me insultando seu padre filho da puta.",
    20: "Eu quero ver você bebendo essa água benta. Beba!",
    21: "Tu és uma piada, padre...me dá logo essa água aqui.",
    22: "FILHO DA PUTA!!!!!!!",
    23: "Eu sou um velho de saia e tu és um pé rapado.",
    24: "Eu sois o capeta, eu vois te provar e tu vais ter teu fim, seu velhão franhudo.",
    25: "Eu vois te provar...eu vois te provar...quando tua hora chegar tu vai queimar.",
    26: "Tu vai queimar igual um leitão pururuca no inferno.",
    27: "Tu vais ter [a prova concreta], tu vais estourar, tu vais agoniar, tu vai pedir pela tua alma.",
    28: "Eu vou comer teu coração na ponta da faca, rapá.",
    29: "Eu sou cruel...eu sou mal...eu sou VAGABUNDO, rapá.",
    30: "Eu sois capeta, seu padre. Eu sois o capeta.",
    31: "Tu tais duvidando de mim desde o começo.",
    32: "Eu vois te trazer tanto pobrema que tu tá ferrado.",
    33: "Eu se proponho a te aniquilar, agora!",
    34: "Tu ousas a me corrigir? Como tu ousas a me corrigirdes?"
}

def make_json(count, index):
    if(int(count) > 20):
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
    print(count)
    random_value = randint(0, 34)
    json_response = json.dumps(make_json(count, random_value))
    return json_response, 200

if __name__ == '__main__':
    app.run(debug=True)