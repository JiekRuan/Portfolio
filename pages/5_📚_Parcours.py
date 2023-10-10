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
    st.header("Parcours Scolaire")
    with st.container():
        left_image, right_text = st.columns((1, 3))
        with left_image:
            st.image("./images/hetic.png")
        with right_text:
            st.header("Bachelor Data & IA")
            st.write("Octobre 2022 - Diplôme prévu 2025")
            hetic_text = """<ul>
                <li>Language de programmation : JavaScript / PHP / SQL / Python</li>
                <li>Librairie python : Pandas / Matplotlib / Seaborn</li>
                <li>UI / UX : Figma</li>
            </ul>"""
            st.markdown(hetic_text, unsafe_allow_html=True)
    with st.container():
        left_image, right_text = st.columns((1, 3))
        with left_image:
            st.image("./images/itic.png")
        with right_text:
            st.header("BTS SIO développement web")
            st.write("Septembre 2021 - juillet 2022")
            ljc_text = """<ul>
                <li>Language de programmation : JavaScript / PHP / SQL / Java</li>
            </ul>"""
            st.markdown(ljc_text, unsafe_allow_html=True)
copyright_footer = """<p>Personnal portfolio for Jiek Ruan &copy 2023</p>"""
st.markdown(copyright_footer, unsafe_allow_html=True)