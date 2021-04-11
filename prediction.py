from sklearn import datasets
from joblib import load
from flask import jsonify
import numpy as np
import json

#load the model

my_model = load('model.pkl')


def my_prediction(hotel,market,deposit_type,month,day,weeknight,weekendnights,adults):
    x = np.array([hotel,market,deposit_type,month,day,weeknight,weekendnights,adults])
    prediction = my_model.predict([x])
    if prediction == 0:
    	prediction = "Will not likely cancel"
    else:
     	prediction = "Will likely cancel"
    return jsonify({"prediction":prediction,"accuracy":"75%"})
