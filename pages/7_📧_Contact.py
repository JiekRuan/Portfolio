import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.app_logo import add_logo
import pandas as pd
import numpy as np
import smtplib
from email.message import EmailMessage

st.set_page_config(page_title="Jiekofolio", page_icon=None, layout="wide")

with open('css/style.css') as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

st.title("Jiek Ruan")

st.header("Contact me")
st.write("Contactez moi sur mon mail jiekruan@gmail.com")
st.write("Vous pouvez également vous connectez avec sur moi différent réseaux :")
st.image("./images/Linkedin.png")
st.image("./images/Github.png")

copyright_footer = """<p>Personnal portfolio for Jiek Ruan &copy 2023</p>"""
st.markdown(copyright_footer, unsafe_allow_html=True)