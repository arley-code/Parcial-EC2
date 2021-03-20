from src import app
from src.controllers.bd import DatabaseController
from flask import make_response, jsonify, request
databaseController = DatabaseController()

@app.route('/basedatos', methods=['GET'])
def databaseList():

    dbs = databaseController.list()
    return make_response(jsonify(dbs), 200)


@app.route('/basedatos', methods=['POST'])
def databaseCreate():

    nombrebd = request.json['nombrebd']

    databaseController.create(nombrebd)

    return make_response('Base de datos creada con exito', 201)

@app.route('/tables/<basedatos>', methods=['GET'])
def tableList(based):

    tables = databaseController.search(based)
    
    return make_response(jsonify(tables), 200)
