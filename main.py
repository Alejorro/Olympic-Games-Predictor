'''
           _____ _____    ____  _                       _      
     /\   |  __ \_   _|  / __ \| |                     (_)     
    /  \  | |__) || |   | |  | | |_   _ _ __ ___  _ __  _  ___ 
   / /\ \ |  ___/ | |   | |  | | | | | | '_ ` _ \| '_ \| |/ __|
  / ____ \| |    _| |_  | |__| | | |_| | | | | | | |_) | | (__ 
 /_/    \_\_|   |_____|  \____/|_|\__, |_| |_| |_| .__/|_|\___|
                                   __/ |         | |           
                                  |___/          |_|       
'''

#Importación de librerías
from flask import Flask, request
from bson.json_util import dumps
import json
import numpy as np
from jinja2 import Template
from flask import render_template
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

#Importación de módulos
from templates import *
from Src.view import *
from Src.cleaner import *
from Src.predict import *

#Inicialización APP:
app = Flask(__name__)

#Inicialización BBDD:
from pymongo import MongoClient
client = MongoClient("mongodb://localhost/OlympicGames")
db = client.get_database()

'''
Endpoints
'''

#Guía principal
@app.route('/', methods=["GET"])
def indexMain():
    return render_template("index.html")


#Enseñar gráficos específicos
@app.route('/plots/<tipo>', methods=["GET"])
def representations(tipo):
    fig = ploting(tipo)
    if type(fig) == tuple:
        return dumps(fig)
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")

#Mostrar dataframes específicos
@app.route('/data/<tipo>', methods=["GET"])
def html_table(tipo):
    df = cleaner(tipo)
    if type(df) == tuple:
        return dumps(df)
    return render_template('simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

#Predicciones
@app.route('/predict', methods=["GET"])
def getPredict():
    userCountry = request.args.get('country')
    exJson = request.args.get('exportJson')
    filtered = filtering(db,userCountry)
    if exJson == "True":
        writeFile =open(f'Output/prediction{userCountry}.json', 'w')
        writeFile.write(str(filtered[0]))
        writeFile.close()
    return dumps(filtered)

#Gestor de errores frecuentes
@app.errorhandler(404)
def handle_notfound(e):
    return 'Page not found'

@app.errorhandler(500)
def handle_intsrverr(e):
    return 'Internal Server Error'

if __name__ == "__main__":
    app.run("0.0.0.0", 4600, debug=True)
