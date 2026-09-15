import streamlit as st
import pandas as pd
import pickle

model=pickle.load(open('model.pkl','rb'))
scaler=pickle.load(open('scaler.pkl','rb'))

st.title('Heart Disease Prediction')

age=st.number_input('Age', min_value=1, max_value=120, value=None)
sex=st.selectbox('Sex', ['Male', 'Female'], index=None, placeholder='select gender')
cp=st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'], index=None, placeholder='select chest pain type')
trestbps=st.number_input('Resting Blood Pressure (in mm Hg)', min_value=80, max_value=200, value=None)
chol=st.number_input('Serum Cholesterol (in mg/dl)', min_value=100, max_value=600, value=None)
fbs=st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['Yes', 'No'], index=None, placeholder='select fasting blood sugar')
restecg=st.selectbox('Resting Electrocardiographic Results', ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'], index=None, placeholder='select resting ECG results')
thalach=st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=None)
exang=st.selectbox('Exercise Induced Angina', ['Yes', 'No'], index=None, placeholder='select exercise induced angina')
oldpeak=st.number_input('ST Depression Induced by Exercise Relative to Rest', min_value=0.0, max_value=10.0, value=None)
male=[1 if sex=='Male' else 0]
non_anginal_pain=[1 if cp=='Non-Anginal Pain' else 0]
typical_angina=[1 if cp=='Typical Angina' else 0]
fbs_yes=[1 if fbs=='Yes' else 0]
restecg_normal=[1 if restecg=='Normal' else 0]
restecg_st_t_wave_abnormality=[1 if restecg=='ST-T Wave Abnormality' else 0]
exang_yes=[1 if exang=='Yes' else 0]

data = pd.DataFrame([[age, trestbps, chol, thalach, oldpeak, male[0], non_anginal_pain[0], typical_angina[0], fbs_yes[0], restecg_normal[0], restecg_st_t_wave_abnormality[0], exang_yes[0]]],
                    columns=['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'male', 'non_anginal_pain', 'typical_angina', 'fbs_yes', 'restecg_normal', 'restecg_st_t_wave_abnormality', 'exang_yes'])
if st.button('Predict'):
    data_scaled = scaler.fit_transform(data)
    prediction = model.predict(data_scaled)
    if prediction[0] == 1 or prediction[0] == 2 or prediction[0] == 3 or prediction[0] == 4:
        st.error('The patient is likely to have heart disease.')
    else:
        st.success('The patient is unlikely to have heart disease.')
    