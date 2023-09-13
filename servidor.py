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


def dataProcessing(infoData):

    #BsmtExposure (TODO: REVISAR)
    if infoData["BsmtExposure"] == "Gd":
        infoData["BsmtExposure"] = 1
    elif infoData["BsmtExposure"] == "Av":
        infoData["BsmtExposure"] = 2
    elif infoData["BsmtExposure"] == "Mn":
        infoData["BsmtExposure"] = 2
    elif infoData["BsmtExposure"] == "No":
        infoData["BsmtExposure"] = 3
    else:
        pass

    #MSZoning
    MSZoning_FV = 0
    MSZoning_RH = 0
    MSZoning_RL = 0
    MSZoning_RM = 0

    if infoData["MSZoning"] == "MSZoning_FV":
        MSZoning_FV = 1
    elif infoData["MSZoning"] == "MSZoning_RH":
        MSZoning_RH = 1
    elif infoData["MSZoning"] == "MSZoning_RL":
        MSZoning_RL = 1
    elif infoData["MSZoning"] == "MSZoning_RM":
        MSZoning_RM = 1
    else:
        pass

    #Neighborhood
    Neighborhood_Crawford = 0
    Neighborhood_Edwards = 0
    Neighborhood_MeadowV = 0
    Neighborhood_NridgHt = 0
    Neighborhood_StoneBr = 0

    if infoData["Neighborhood"] == "Neighborhood_Crawfor":
        Neighborhood_Crawford = 1
    elif infoData["Neighborhood"] == "Neighborhood_Edwards":
        Neighborhood_Edwards = 1
    elif infoData["Neighborhood"] == "Neighborhood_MeadowV":
        Neighborhood_MeadowV = 1
    elif infoData["Neighborhood"] == "Neighborhood_NridgHt":
        Neighborhood_NridgHt = 1
    elif infoData["Neighborhood"] == "Neighborhood_StoneBr":
        Neighborhood_StoneBr = 1
    else:
        pass

    #Condition1
    Condition1_Artery = 0
    Condition1_Feedr = 0
    Condition1_RRAe = 0
    Condition2_PosA = 0
    Condition2_PosN = 0

    if infoData["Condition1"] == "Condition1_Artery":
        Condition1_Artery = 1
    elif infoData["Condition1"] == "Condition1_Feedr":
        Condition1_Feedr = 1
    elif infoData["Condition1"] == "Condition1_RRAe":
        Condition1_RRAe = 1
    elif infoData["Condition1"] == "Condition2_PosA": 
        Condition2_PosA = 1
    elif infoData["Condition1"] == "Condition2_PosN":     
        Condition2_PosN = 1
    else:
        pass

    #BldgType
    BldgType_Twnhs = 0
    BldgType_TwnhsE = 0

    if infoData["BldgType"] == "BldgType_Twnhs":
        BldgType_Twnhs = 1
    elif infoData["BldgType"] == "BldgType_TwnhsE":
        BldgType_TwnhsE = 1
    else:
        pass

    #RoofMatl
    RoofMatl_ClyTile = 0
    RoofMatl_CompShg = 0

    if infoData["RoofMatl"] == "RoofMatl_ClyTile":
        RoofMatl_ClyTile = 1
    elif infoData["RoofMatl"] == "RoofMatl_CompShg":
        RoofMatl_CompShg = 1
    else:
        pass

    #Exterior1st
    Exterior1st_BrkComm = 0
    Exterior1st_BrkFace = 0
    Exterior1st_MetalSd = 0

    if infoData["Exterior1st"] == "Exterior1st_BrkComm":
        Exterior1st_BrkComm = 1
    elif infoData["Exterior1st"] == "Exterior1st_BrkFace":
        Exterior1st_BrkFace = 1
    elif infoData["Exterior1st"] == "Exterior1st_MetalSd":
        Exterior1st_MetalSd = 1
    else:
        pass

    #Foundation
    Foundation_BrkTil = 0
    Foundation_CBlock = 0
    Foundation_Wood = 0

    if infoData["Foundation"] == "Foundation_BrkTil":
        Foundation_BrkTil = 1
    elif infoData["Foundation"] == "Foundation_CBlock":
        Foundation_CBlock = 1
    elif infoData["Foundation"] == "Foundation_Wood":
        Foundation_Wood = 1
    else:
        pass

    #Heating
    Heating_GasA = 0
    Heating_Grav = 0

    if infoData["Heating"] == "Heating_GasA":
        Heating_GasA = 1
    elif infoData["Heating"] == "Heating_Grav":
        Heating_Grav = 1
    else:
        pass

    #Functional
    Functional_Maj1 = 0
    Functional_Min1 = 0
    Functional_Min2 = 0
    Functional_Mod = 0
    Functional_Typ = 0

    if infoData["Functional"] == "Functional_Maj1":
        Functional_Maj1 = 1
    elif infoData["Functional"] == "Functional_Min1":
        Functional_Min1 = 1
    elif infoData["Functional"] == "Functional_Min2":
        Functional_Min2 = 1
    elif infoData["Functional"] == "Functional_Mod":
        Functional_Mod = 1
    elif infoData["Functional"] == "Functional_Typ":
        Functional_Typ = 1
    else:
        pass

    #SaleType
    SaleType_COD = 0
    SaleType_ConLI = 0
    SaleType_WD = 0

    if infoData["SaleType"] == "SaleType_COD":
        SaleType_COD = 1
    elif infoData["SaleType"] == "SaleType_ConLI":
        SaleType_ConLI = 1
    elif infoData["SaleType"] == "SaleType_WD":
        SaleType_WD = 1
    else:
        pass

    
    return infoData.update({
        "MSZoning_FV": MSZoning_FV,
        "MSZoning_RH": MSZoning_RH,
        "MSZoning_RL": MSZoning_RL,
        "MSZoning_RM": MSZoning_RM,
        "Neighborhood_Crawford": Neighborhood_Crawford,
        "Neighborhood_Edwards": Neighborhood_Edwards,
        "Neighborhood_MeadowV": Neighborhood_MeadowV,
        "Neighborhood_NridgHt": Neighborhood_NridgHt,
        "Neighborhood_StoneBr": Neighborhood_StoneBr,
        "Condition1_Artery": Condition1_Artery,
        "Condition1_Feedr": Condition1_Feedr,
        "Condition1_RRAe": Condition1_RRAe,
        "Condition2_PosA": Condition2_PosA,
        "Condition2_PosN": Condition2_PosN,
        "BldgType_Twnhs": BldgType_Twnhs,
        "BldgType_TwnhsE": BldgType_TwnhsE,
        "RoofMatl_ClyTile": RoofMatl_ClyTile,
        "RoofMatl_CompShg": RoofMatl_CompShg,
        "Exterior1st_BrkComm": Exterior1st_BrkComm,
        "Exterior1st_BrkFace": Exterior1st_BrkFace,
        "Exterior1st_MetalSd": Exterior1st_MetalSd,
        "Foundation_BrkTil": Foundation_BrkTil,
        "Foundation_CBlock": Foundation_CBlock,
        "Foundation_Wood": Foundation_Wood,
        "Heating_GasA": Heating_GasA,
        "Heating_Grav": Heating_Grav,
        "Functional_Maj1": Functional_Maj1,
        "Functional_Min1": Functional_Min1,
        "Functional_Min2": Functional_Min2,
        "Functional_Mod": Functional_Mod,
        "Functional_Typ": Functional_Typ,
        "SaleType_COD": SaleType_COD,
        "SaleType_ConLI": SaleType_ConLI,
        "SaleType_WD": SaleType_WD
    })


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
            infoData["LotArea"],
            1,
            1,
            infoData["YearBuilt"],
            1, # TODO: REVISAR
            infoData["BsmtExposure"], #TODO:REVISAR
            infoData["BsmtFinSF1"],
            infoData["TotalBsmtSF"],
            1,
            infoData["CentralAir"],
            infoData["GrLivArea"],
            infoData["BsmtFullBath"],
            infoData["HalfBath"],
            infoData["KitchenAbvGr"],
            1,
            infoData["Fireplaces"],
            infoData["GarageCars"],
            1,
            infoData["WoodDeckSF"],
            infoData["ScreenPorch"],
            infoData["MSZoning_FV"],
            infoData["MSZoning_RH"],
            infoData["MSZoning_RL"],
            infoData["MSZoning_RM"],
            infoData["LotConfig_Inside"],
            infoData["LandSlope_Sev"],
            infoData["Neighborhood_Crawford"],
            infoData["Neighborhood_Edwards"],
            infoData["Neighborhood_MeadowV"],
            infoData["Neighborhood_NridgHt"],
            infoData["Neighborhood_StoneBr"],
            infoData["Condition1_Artery"],
            infoData["Condition1_Feedr"],
            infoData["Condition1_RRAe"],
            infoData["Condition2_PosA"],
            infoData["Condition2_PosN"],
            infoData["BldgType_Twnhs"],
            infoData["BldgType_TwnhsE"],
            infoData["RoofMatl_ClyTile"],
            infoData["RoofMatl_CompShg"],
            infoData["Exterior1st_BrkComm"],
            infoData["Exterior1st_BrkFace"],
            infoData["Exterior1st_MetalSd"],
            infoData["Exterior2nd_BrkFace"],
            infoData["Foundation_BrkTil"],
            infoData["Foundation_CBlock"],
            infoData["Foundation_Wood"],
            infoData["Heating_GasA"],
            infoData["Heating_Grav"],
            infoData["Electrical_SBrkr"],
            infoData["Functional_Maj1"],
            infoData["Functional_Min1"],
            infoData["Functional_Min2"],
            infoData["Functional_Mod"],
            infoData["Functional_Typ"],
            infoData["GarageType_2Types"],
            infoData["SaleType_COD"],
            infoData["SaleType_ConLI"],
            infoData["SaleType_WD"],
            infoData["SaleCondition_Normal"],
        ]
    )

    print("Datos en array: \n", datos_array, "\n")
    # Predecir el valor de la calidad del vino
    prediccion = dt.predict(datos_array.reshape(1, -1))

    # Retornar la predicción en formato JSON
    return jsonify({"prediccion": str(prediccion[0])})


if __name__ == "__main__":
    servidorWeb.run(debug=False, host="0.0.0.0", port="8080")
