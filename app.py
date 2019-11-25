from flask import *
import json
from os import path


app = Flask(__name__)

# _______________  Fonctions ____________
def readData():
    with open('test.json') as json_file:
        datafile = json.load(json_file)
    return datafile


def putData(data):
    if path.exists('test.json'):
        with open('test.json') as json_file:
            datafile = json.load(json_file)

        jdata = json.loads(data)
        adata = jdata["test2"]
        print(adata)
        datafile["test2"].append(adata)

        with open('test.json', 'w') as outfile:
            json.dump(datafile, outfile)
        process = 'True'
    else:
        process = 'False'
    return process


# _______________  ROUTES _______________

@app.route('/v1/hello-world')
def hello_world():
    return 'Hello World!'


@app.route('/data', methods=['GET'])
def parse_request1():
    # Votre fonction pour lire les data d'un fichier
    data = readData()
    return data


@app.route('/data', methods=['POST'])
def parse_request2():
    data = request.data  # Le payload de votre requete
    print(str(data))
    result = putData(data)
    return result


if __name__ == '__main__':
    app.run()
    # app.run("0.0.0.0")
