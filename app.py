import streamlit as st

main_page = st.Page("Home.py", title="Health Prediction App", icon="🏥")
page_2 = st.Page("pages/heart.py", title="Heart Disease Prediction", icon="❤️")
page_3 = st.Page("pages/diabetes.py", title="Diabetes Prediction", icon="🩸")

pg = st.navigation([main_page, page_2, page_3])
if "lang" not in st.session_state:
    st.session_state.lang = "EN"

st.session_state.lang = st.sidebar.selectbox(
    "Select Language",
    ("EN", "ID"),
    index=("EN","ID").index(st.session_state.lang)
)

pg.run()
    
