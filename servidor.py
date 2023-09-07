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
    # Recibir los datos de la petición
    datos = request.json
    print(datos)
    # Convertir los datos en un array
    datos_array = np.array([
        0.88, 0, 2.6, 0.098, 25, 67, 0.9968, 1, 0.4,
        datos['ph'],
        datos['sulfato'],
        datos['alcohol'],
    ])
    # Predecir el valor de la calidad del vino
    prediccion = dt.predict(datos_array.reshape(1, -1))

    # Retornar la predicción en formato JSON
    return jsonify({'prediccion': str(prediccion[0])})

if __name__ == '__main__':
    servidorWeb.run(debug=False, host='0.0.0.0', port='8080')