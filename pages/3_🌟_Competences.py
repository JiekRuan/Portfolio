import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.app_logo import add_logo
import pandas as pd
import numpy as np

st.set_page_config(page_title="Jiekofolio", page_icon=None, layout="wide")

with open('css/style.css') as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

st.title("Jiek Ruan")

with st.container():
    st.title("Compétences")
    with st.container():
        left, right = st.columns((1,3))
        with left:
            st.write("Language de programmation")
            st.write("Framework Python")
            st.write("Librairie Python")
            st.write("Gestion de base de donnée")
            st.write("Front-End UI/UX")
            st.write("Data Viz")
            st.write("Outil no code")
        with right:
            st.write("Python - SQL - JavaScript")
            st.write("Streamlit - FastAPI")
            st.write("Pandas - Maplotlib - Seaborn")
            st.write("MySQL - PGAdmin")
            st.write("Figma - HTML - CSS")
            st.write("Power Bi")
            st.write("Wordpress - Webflow")

copyright_footer = """<p>Personnal portfolio for Jiek Ruan &copy 2023</p>"""
st.markdown(copyright_footer, unsafe_allow_html=True)