import streamlit as st
from utils.dictionary import text

lang = st.session_state.lang

st.markdown(
    f"""
    <h1 style='text-align:center; color:#2E86C1;'>
    {text['title'][lang]}
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <h4 style='text-align:center; color:gray;'>
    {text['home_desc'][lang]}
    </h4>
    """,
    unsafe_allow_html=True
)

st.divider()

st.markdown(
f"""
### {text['feature_title'][lang]}
- {text['diabetes_feature'][lang]}
- {text['heart_feature'][lang]}
"""
)

st.write("")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    ### Diabetes Prediction

    {text['diabetes_feature'][lang]}

    - Glucose
    - BMI
    - Insulin
    - Age
    """)

    st.page_link(
        "pages/diabetes.py",
        label="***Start Diabetes Prediction***",
    )


with col2:
    st.markdown(f"""
    ### Heart Disease Prediction

    {text['heart_feature'][lang]}

    - Age
    - Blood Pressure
    - Cholesterol
    """)

    st.page_link(
        "pages/heart.py",
        label="***Start Heart Prediction***",
    )


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