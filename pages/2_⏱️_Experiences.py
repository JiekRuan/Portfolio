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
    st.header("Expériences")
    with st.container():
        left_image, right_text = st.columns((1, 3))
        with left_image:
            st.image("./images/KK.png")
        with right_text:
            st.header("Développeur Wordpress")
            st.write("Stage : avril 2022 - juin 2022")
            kk_text = """<ul>
                <li>Analyse du cahier des charges pour une mise à jour du site vitrine</li>
                <li>Maquette et wireframes réalisé avec Figma</li>
                <li>Application de la maquette sur Wordpress</li>
            </ul>"""
            st.markdown(kk_text, unsafe_allow_html=True)
    with st.container():
        left_image, right_text = st.columns((1, 3))
        with left_image:
            st.image("./images/LJC.png")
        with right_text:
            st.header("Développeur Full Stack")
            st.write("Stage : juin 2021 - août 2021")
            ljc_text = """<ul>
                <li>Analyse du cahier des charges pour une app mobile de click&collect </li>
                <li>Benchmark et Constitution des wireframes pour l'application</li>
                <li>Création d une base de donnée avec Postgresql</li>
                <li>Application du site avec Vuejs et Expressjs</li>
            </ul>"""
            st.markdown(ljc_text, unsafe_allow_html=True)
copyright_footer = """<p>Personnal portfolio for Jiek Ruan &copy 2023</p>"""
st.markdown(copyright_footer, unsafe_allow_html=True)
