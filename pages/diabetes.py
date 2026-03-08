import streamlit as st
import pandas as pd
import joblib
from utils.dictionary import text

lang = st.session_state.lang
st.set_page_config(page_title="Diabetes Prediction", layout="centered")
model = joblib.load("model/diabetes_model")

st.title(text["diabetes"][lang])
Pregnancies = st.number_input(text["pregnancies"][lang], min_value=0, max_value=20, value=0)
Glucose = st.number_input(text["glucose"][lang], min_value=0, max_value=300, value=0)
BloodPressure = st.number_input(text["blood_pressure"][lang], min_value=0, max_value=200, value=0)
Insulin = st.number_input(text["insulin"][lang], min_value=0, max_value=900, value=0)
BMI = st.number_input(text["bmi"][lang], min_value=0.0, max_value=70.0, value=0.0)
DiabetesPedigreeFunction = st.number_input(text["pedigree"][lang], min_value=0.0, max_value=2.5, value=0.0)
Age = st.number_input(text["age"][lang], min_value=0, max_value=120, value=0)

if st.button(text["predict"][lang]):
    data = pd.DataFrame({
    "Pregnancies":[Pregnancies],
    "Insulin":[Insulin],
    "BMI":[BMI],
    "Age":[Age],
    "Glucose":[Glucose],
    "BloodPressure":[BloodPressure],
    "DiabetesPedigreeFunction":[DiabetesPedigreeFunction]
})
    prediction = model.predict(data)
    if prediction[0] == 1:
        st.error("Diabetes Detected")
    else:
        st.success("No Diabetes Detected")

st.divider()

st.markdown(
"""
<div style='text-align:center; font-size:14px; color:gray'>

🏥 <b>Health Prediction App</b><br>
Machine Learning Web App for Disease Prediction

<br>

Created by <b>VuniSek</b>

<a href="https://github.com/VuniSek" target="_blank" style="text-decoration:none; color:gray;">
<svg height="22" viewBox="0 0 16 16" width="22" fill="currentColor" style="vertical-align:middle;">
<path d="M8 0C3.58 0 0 3.58 0 8a8 8 0 0 0 5.47 7.59c.4.07.55-.17.55-.38
0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13
-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66
.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95
0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12
0 0 .67-.21 2.2.82a7.6 7.6 0 0 1 2-.27c.68 0 1.36.09
2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08
2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65
3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2
0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
</svg>

&nbsp; GitHub
</a>

</div>
""",
unsafe_allow_html=True
)