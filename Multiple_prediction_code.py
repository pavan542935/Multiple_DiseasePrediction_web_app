# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 09:32:14 2025

@author: saipa
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loding the saved models

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

parkinsons_model= pickle.load(open('Parkinsons_model.sav','rb'))


#side barfor navagetion

with st.sidebar:
    
    selected = option_menu('Multiple disease predection system', ['Diabetes Prediction',
                                                                  'Heart Disease Prediction',
                                                                  'Parkinsons Disease prediction'],
                                                                   icons =['activity','heart','person'],
                                                                    default_index = 0)
     
    
    
#diabetes prediction page

if(selected == 'Diabetes Prediction'):
    
    #page title
    st.title("Diabetes Prediction using ml")
    
    col1,col2,col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
         Glucose = st.text_input('Glucose Level')
    with col3:
         BloodPressure = st.text_input('BloodPressure Level')
    with col1:
          SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
         Insulin = st.text_input('Insulin Level')
    with col3:
         BMI = st.text_input('BMI value')
    with col1:
         DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction Level')
    with col2:
        Age = st.text_input('Age of the person')
    
    #code for prediction
    diab_dignosis = ''
    
    #creating a button 
    if st.button('Diabetes Test Results'):
        dia_prediction = diabetes_model.predict([[Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin, BMI,DiabetesPedigreeFunction,Age]])
        if(dia_prediction[0] == 1):
            diab_dignosis = 'THE PERSION IS DIABETIC'
            
        else:
            diab_dignosis = 'THE PERSION IS NOT DIABETIC'
            
    st.success(diab_dignosis)

    
if(selected == 'Heart Disease Prediction'):
    
    #page title
    st.title("Heart disease Prediction using ml")
    
    
    #age


    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.text_input("Enter your age")
    with col2:
       sex = st.text_input('Enter the sex')
    with col3:
        cp = st.text_input('Enter the cp')
    with col1:
        trestbps = st.text_input("Enter the trestbps")
    with col2:
        chol = st.text_input("Enter the chol")
    with col3:
        fbs = st.text_input("Enter the fbs value")
    with col1:
        restecg = st.text_input("Enter the restecg")
    with col2:
        thalach = st.text_input("Enter the thalach")
    with col3:
        exang = st.text_input("enter the exang")
    with col1:
        oldpeak = st.text_input("Enter the oldpeak")
    with col2:
        slope = st.text_input("Enter the slope")
    with col3:
        ca = st.text_input("Enter the ca")
    with col1:
        thal = st.text_input("Ener the thal")
        
        
    heart_dignosis = ''
    
    if st.button("Heart diseas test Results"):
        hea_predict = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if hea_predict[0] == 0:
            heart_dignosis = 'THE PERSION HAS NO HEART DISEASE '
        else:
            heart_dignosis = 'THE PERSION HAS HEART DISEASE'
    st.success(heart_dignosis)
    
    

    
    
if(selected == 'Parkinsons Disease prediction'):
    
    #page title
    st.title("Parkinsons Disease prediction using ml")
    

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")
        
    with col1:
        jitter_percent = st.text_input("MDVP:Jitter(%)")
    with col2:
         jitter_abs = st.text_input("MDVP:Jitter(Abs)")
    with col3:
         rap = st.text_input("MDVP:RAP")
         
    with col1:
         ppq = st.text_input("MDVP:PPQ")
    with col2:
         ddp = st.text_input("Jitter:DDP")
    with col3:
         shimmer = st.text_input("MDVP:Shimmer")

    with col1:
        shimmer_db = st.text_input("MDVP:Shimmer(dB)")
    with col2:
       apq3 = st.text_input("Shimmer:APQ3")
    with col3:
       apq5 = st.text_input("Shimmer:APQ5")

    with col1:
        mdvp_apq = st.text_input("MDVP:APQ")
    with col2:
        dda = st.text_input("Shimmer:DDA")
    with col3:
        nhr = st.text_input("NHR")

    with col1:
        hnr = st.text_input("HNR")
    with col2:
        rpde = st.text_input("RPDE")
    with col3:
        dfa = st.text_input("DFA")

    with col1:
        spread1 = st.text_input("spread1")
    with col2:
        spread2 = st.text_input("spread2")
    with col3:
        d2 = st.text_input("D2")

    with col1:
        ppe = st.text_input("PPE")
        
    
    parkinsons_dignosis = ''
    
    if st.button("parkinsons test Results"):
        par_predict = parkinsons_model.predict([[fo,fhi,flo,jitter_percent,jitter_abs,rap,ppq,ddp,shimmer,shimmer_db,apq3,apq5,mdvp_apq,dda,nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe
]])
        if par_predict[0] == 0:
            parkinsons_dignosis = 'THE PERSION HAS NO Parkinsons Disease '
        else:
            parkinsons_dignosis = 'THE PERSION HAS Parkinsons DISEASE'
    st.success(parkinsons_dignosis)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    