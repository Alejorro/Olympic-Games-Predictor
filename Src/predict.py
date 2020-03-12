#Importación de librerías
from pymongo import MongoClient
from bson.json_util import dumps
import json

#Importación de módulos
from Src.errorHandler import *

@jsonErrorHandler
def filtering(db, country):
    client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
    filter={'Region': f'{country}'}
    project={'_id': 0,'Region': 1,'predict': 1}

    result = client['OlympicGames']['Predicted'].find(filter=filter,projection=project)

    try:
        if len(list(result[0])):
            return result

    except:
        raise Exception("Pais mal introducido, consulte el manual")


    

        