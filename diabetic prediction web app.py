# -*- coding: utf-8 -*-
"""
Created on Mon May 22 13:17:13 2023

@author: santo
"""

import numpy as np
import pickele
import streamlit  as st

# loading the saved model
loaded_model = pickle.load(open('D:\project_56_62/trained_model.sav', 'rb'))

#creating a function for prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return'The person is diabetic'

def main():
    
    # giving 
    st.title('Diabetes Prediction Web App')
    
    #getting the input data from the user
    Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction
    