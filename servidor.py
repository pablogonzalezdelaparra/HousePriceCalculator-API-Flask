from flask import Flask, render_template, request, jsonify
import numpy as np
from joblib import load
import os

# Cargar el modelo
dt=load('dt1.joblib')

# Generar el servidor (Back End)

servidorWeb = Flask(__name__)

# Ruta para entrenar el modelo
@servidorWeb.route("/entrenar", methods=['GET'])
def entrenar():
    # Llamar wine_quality.py para entrenar el modelo
    os.system('python wine_quality.py')
    return jsonify({'resultado': 'ok'})

@servidorWeb.route("/holamundo", methods=['GET'])
def holaMundo():
    return render_template('pagina1.html')

# Envío de datos a través de JSON
@servidorWeb.route("/modelo", methods=['POST'])
def modelo():
    # Recibir los datos de la petición
    datos = request.get_json(force=True)
    # Convertir los datos en un array
    datos_array = np.array(datos['datos'])
    # Predecir el valor de la calidad del vino
    prediccion = dt.predict(datos_array)
    # Retornar la predicción en formato JSON
    return jsonify({'prediccion': prediccion.tolist()})

if __name__ == '__main__':
    servidorWeb.run(debug=False, host='0.0.0.0', port='8080')