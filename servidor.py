from flask import Flask, render_template, request, jsonify
import numpy as np
from joblib import load
import os

# Cargar el modelo
dt=load('dt1.joblib')

# Generar el servidor (Back End)

servidorWeb = Flask(__name__)

@servidorWeb.route("/holamundo", methods=['GET'])
def holaMundo():
    return render_template('pagina1.html')

# Envío de datos a través de JSON
@servidorWeb.route("/modelo", methods=['POST'])
def modelo():
    contenido = request.json
    print(contenido)
    return jsonify({'resultado': 'ok'})

if __name__ == '__main__':
    servidorWeb.run(debug=False, host='0.0.0.0', port='8080')