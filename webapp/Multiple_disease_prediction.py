import numpy as np
import streamlit as st
import pickle
from streamlit_option_menu import option_menu



diabetes_model=pickle.load(open("E:\\MACHINE LEARNING PROJECTS\\DISEASE PREDICTIONS\\webapp\\diabetes_model.pkl",'rb')) 
heart_disease_model=pickle.load(open("E:\\MACHINE LEARNING PROJECTS\\DISEASE PREDICTIONS\\webapp\\heart_model.pkl",'rb')) 
parkinson_model = pickle.load(open("E:\\MACHINE LEARNING PROJECTS\\DISEASE PREDICTIONS\\webapp\\parkinson_model.pkl",'rb'))


with st.sidebar:
    selected=option_menu("Multiple Disease Prediction System",
                         ["Diabetes Prediction","Heart Disease Prediction","Parkinsons Prediction"],
                         icons=['activity','heart','person'],
                         default_index=0)
if selected=='Diabetes Prediction':
    st.title("Diabetes Prediction")
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input("Number of pregnancies")
    with col2:
        Glucose=st.text_input("Glucose Level")
    with col3:
        BloodPressure=st.text_input("Blood Pressure Level")
    with col1:
        SkinThickness=st.text_input("Skin Thickness Level")
    with col2:
        Insulin=st.text_input("Insulin Level")
    with col3:
        BMI=st.text_input("BMI Level")
    with col1:
        DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function Level")
    with col2:
        Age=st.text_input("Enter your age")


    
    
    if st.button("Predict"):
        
        diab_diagnosis=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if diab_diagnosis[0] == 1:
            st.error("You are likely to have Diabetes")
        else:
             st.success("You dont have diabetes")

if selected=="Heart Disease Prediction":
    st.title("Heart Disease Prediction")

    
    col1,col2,col3,col4=st.columns(4)
    
    with col1:
        age=st.text_input("Enter the age")
    with col2:
        sex=st.text_input("Enter the gender")
    with col3:
         cp=st.text_input("Enter the cp value")
    with col4:
         trestbps=st.text_input("Enter the trestbps value")
    with col1:
        chol=st.text_input("Enter the cholesterol level")
    with col2:
        fbs=st.text_input("Enter the Fasting blood sugar (FBS) level")
    with col3:
        restecg=st.text_input("Enter the resting electrocardiographic value")
    with col4:
        thalach=st.text_input("Enter the thalach value")
    with col1:
        exang=st.text_input("Enter the exang value")
    with col2:
        oldpeak=st.text_input("Enter the oldpeak value")
    with col3:
        slope=st.text_input("Enter the slope value")
    with col4:
        ca=st.text_input("Enter the ca value")
    with col1:
        thal=st.text_input("Enter the thalassemia value")

    heart_disease_diagnosis=''
    if st.button("Predict"):
        age = int(age)
        sex = int(sex)
        cp = int(cp)
        trestbps = int(trestbps)
        chol = int(chol)
        fbs = int(fbs)
        restecg = int(restecg)
        thalach = int(thalach)
        exang = int(exang)
        oldpeak = float(oldpeak)
        slope = int(slope)
        ca = int(ca)
        thal = int(thal)

        heart_disease_diagnosis=heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if heart_disease_diagnosis[0]==1:
            st.error("You may have heart disease")
        else:
            st.success("You dont have heart disease")


if selected == "Parkinsons Prediction":
    st.title("Parkinsons Prediction")

    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        mdvp_fo = st.text_input("Enter the MDVP:Fo(Hz) value")
    with col2:
        mdvp_fhi = st.text_input("Enter the MDVP:Fhi(Hz) value")
    with col3:
        mdvp_flo = st.text_input("Enter the MDVP:Flo(Hz) value")
    with col4:
        mdvp_jitter_percent = st.text_input("Enter the MDVP:Jitter(%) value")
    with col5:
        mdvp_jitter_abs = st.text_input("Enter the MDVP:Jitter(Abs) value")
    with col1:
        mdvp_rap = st.text_input("Enter the MDVP:RAP value")
    with col2:
        mdvp_ppq = st.text_input("Enter the MDVP:PPQ value")
    with col3:
        jitter_ddp = st.text_input("Enter the Jitter:DDP value")
    with col4:
        mdvp_shimmer = st.text_input("Enter the MDVP:Shimmer value") 
    with col5:
        mdvp_shimmer_db = st.text_input("Enter the MDVP:Shimmer(dB) value")
    with col1:
        shimmer_apq3 = st.text_input("Enter the Shimmer:APQ3 value")
    with col2:
        shimmer_apq5 = st.text_input("Enter the Shimmer:APQ5 value")
    with col3:
        mdvp_apq = st.text_input("Enter the MDVP:APQ value")
    with col4:
        shimmer_dda = st.text_input("Enter the Shimmer:DDA value")
    with col5:
        nhr = st.text_input("Enter the NHR value")
    with col1:
        hnr = st.text_input("Enter the HNR value")
    with col2:
        rpde = st.text_input("Enter the RPDE value")
    with col3:
        dfa = st.text_input("Enter the DFA value")
    with col4:
        spread1 = st.text_input("Enter the spread1 value")
    with col5:
        spread2 = st.text_input("Enter the spread2 value")
    with col1:
        d2 = st.text_input("Enter the D2 value")
    with col2:
        ppe = st.text_input("Enter the PPE value")
   
    parkinson_diagnosis = ''
    
    if st.button("Predict"):
        try:
            inputs = [float(mdvp_fo), float(mdvp_fhi), float(mdvp_flo), float(mdvp_jitter_percent), 
                      float(mdvp_jitter_abs), float(mdvp_rap), float(mdvp_ppq), float(jitter_ddp), 
                      float(mdvp_shimmer), float(mdvp_shimmer_db), float(shimmer_apq3), float(shimmer_apq5), 
                      float(mdvp_apq), float(shimmer_dda), float(nhr), float(hnr), 
                      float(rpde), float(dfa), float(spread1), float(spread2), 
                      float(d2), float(ppe)]
            
            parkinson_diagnosis = parkinson_model.predict([inputs])
            
            if parkinson_diagnosis[0] == 1:
                st.error("You may have Parkinson's disease")
            else:
                st.success("You don't have Parkinson's disease")
        except ValueError:
            st.error("Please enter valid numeric values")
