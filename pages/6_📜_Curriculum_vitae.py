import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.app_logo import add_logo
import pandas as pd
import numpy as np

st.set_page_config(page_title="Jiekofolio", page_icon=None, layout="wide")

with open('css/style.css') as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

st.title("Jiek Ruan")

st.header("Curriculum Vitae")

st.image("./images/cv.png")

cv_pdf_link = 'Jiek_ruan_data_analyst_cv'
st.markdown(f"**[Télécharger le CV]({cv_pdf_link})**", unsafe_allow_html=True)

copyright_footer = """<p>Personnal portfolio for Jiek Ruan &copy 2023</p>"""
st.markdown(copyright_footer, unsafe_allow_html=True)

