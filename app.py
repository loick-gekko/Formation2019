from flask import *

app = Flask(__name__)

#_______________  Fonctions ____________
def readData():
    json = ""
    return json


def putData(data):
    process = False


    return process


#_______________  ROUTES _______________

@app.route('/v1/hello-world')
def hello_world():
    return 'Hello World!'


@app.route('/data', methods=['GET'])
def parse_request():
    # Votre fonction pour lire les data d'un fichier

    data = readData()
    return data

@app.route('/data', methods=['POST'])
def parse_request():
    data = request.data  # Le payload de votre requete
    result = putData(data)
    return result

if __name__ == '__main__':
    app.run("0.0.0.0")
