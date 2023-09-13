from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from joblib import load
import os

# Cargar el modelo
dt = load("HousesRandomForest.joblib")

# Generar el servidor (Back End)
servidorWeb = Flask(__name__)

# Enable CORS for all routes
CORS(servidorWeb, resources={r"/*": {"origins": "*"}})


def dataProcessing():
    """
    datos_array = np.array(
        [
            infoData.LotArea,
            1,
            1,
            infoData.YearBuilt,
            infoData.YearRemodAdd,
            infoData.BsmtExposure,
            infoData.BsmtFinSF1,
            infoData.TotalBsmtSF,
            1,
            infoData.CentralAir,
            infoData.GrLivArea,
            infoData.BsmtFullBath,
            infoData.HalfBath,
            infoData.KitchenAbvGr,
            1,
            infoData.Fireplaces,
            infoData.GarageCars,
            1,
            infoData.WoodDeckSF,
            infoData.ScreenPorch,
            MSZoning_FV,
            MSZoning_RH,
            MSZoning_RL,
            MSZoning_RM,
            infoData.LotConfig_Inside,
            infoData.LandSlope_Sev,
            Neighborhood_Crawford,
            Neighborhood_Edwards,
            Neighborhood_MeadowV,
            Neighborhood_NridgHt,
            Neighborhood_StoneBr,
            Condition1_Artery,
            Condition1_Feedr,
            Condition1_RRAe,
            Condition2_PosA,
            Condition2_PosN,
            BldgType_Twnhs,
            BldgType_TwnhsE,
            RoofMatl_ClyTile,
            RoofMatl_CompShg,
            Exterior1st_BrkComm,
            Exterior1st_BrkFace,
            Exterior1st_MetalSd,
            infoData.Exterior2nd_BrkFace,
            Foundation_BrkTil,
            Foundation_CBlock,
            Foundation_Wood,
            Heating_GasA,
            Heating_Grav,
            infoData.Electrical_SBrkr,
            Functional_Maj1,
            Functional_Min1,
            Functional_Min2,
            Functional_Mod,
            Functional_Typ,
            infoData.GarageType_2Types,
            SaleType_COD,
            SaleType_ConLI,
            SaleType_WD,
            infoData.SaleCondition_Normal,
        ]
    )
    """
    pass


# Envío de datos a través de JSON
@servidorWeb.route("/model/getPrediction", methods=["POST"])
def modelo():
    # Recibir los datos de la petición
    infoData = request.json
    print("Datos: \n", infoData, "\n")

    # Preprocesamiento de los datos
    dataProcessing(infoData)

    # Convertir los datos en un array
    datos_array = np.array(
        [
            infoData.LotArea,
            1,
            1,
            infoData.YearBuilt,
            infoData.YearRemodAdd,
            infoData.BsmtExposure,
            infoData.BsmtFinSF1,
            infoData.TotalBsmtSF,
            1,
            infoData.CentralAir,
            infoData.GrLivArea,
            infoData.BsmtFullBath,
            infoData.HalfBath,
            infoData.KitchenAbvGr,
            1,
            infoData.Fireplaces,
            infoData.GarageCars,
            1,
            infoData.WoodDeckSF,
            infoData.ScreenPorch,
            1,
            1,
            1,
            1,
            infoData.LotConfig_Inside,
            infoData.LandSlope_Sev,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            infoData.Exterior2nd_BrkFace,
            1,
            1,
            1,
            1,
            1,
            infoData.Electrical_SBrkr,
            1,
            1,
            1,
            1,
            1,
            infoData.GarageType_2Types,
            1,
            1,
            1,
            infoData.SaleCondition_Normal,
        ]
    )

    print("Datos en array: \n", datos_array, "\n")
    # Predecir el valor de la calidad del vino
    prediccion = dt.predict(datos_array.reshape(1, -1))

    # Retornar la predicción en formato JSON
    return jsonify({"prediccion": str(prediccion[0])})


if __name__ == "__main__":
    servidorWeb.run(debug=False, host="0.0.0.0", port="8080")
