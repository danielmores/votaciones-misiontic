from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve


app=Flask(__name__)
cors = CORS(app)
from Controladores.MesasControlador import MesasControlador
from Controladores.VotosControlador import VotosControlador
from Controladores.CandidatosControlador import CandidatosControlador

miControladorMesa=MesasControlador()
controladorVoto = VotosControlador()
candidatoControlador = CandidatosControlador()
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
@app.route("/mesas",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)
@app.route("/mesas",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['GET'])
def getMesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id, data)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)





@app.route("/votos",methods=['GET'])
def getVotos():
    json=controladorVoto.index()
    return jsonify(json)

@app.route("/votos",methods=['POST'])
def crearVoto():
    data = request.get_json()
    json=controladorVoto.create(data)
    return jsonify(json)

@app.route("/votos/<string:id>",methods=['GET'])
def getVoto(id):
    json=controladorVoto.show(id)
    return jsonify(json)





@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    json=candidatoControlador.index()
    return jsonify(json)

@app.route("/candidatos",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=candidatoControlador.create(data)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    json=candidatoControlador.show(id)
    return jsonify(json)






def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])