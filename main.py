#Importaciones
from flask import Flask, request
from pymongo import MongoClient
from bson.json_util import dumps
import json

from Src.view import *

#Inicialización APP:
app = Flask(__name__)

#Endpoints
@app.route('/historic/plots/<tipo>')
def representations(tipo):
    chooseRepr = request.args.get('repr')
    output = view(tipo, chooseRepr)

    return 


@app.route('/historic/plots/<tipo>')
def showResults(tipo):
    chooseRepr = request.args.get('repr')
    output = view(tipo, chooseRepr)

    return 


app.run("0.0.0.0", 4500, debug=True)
