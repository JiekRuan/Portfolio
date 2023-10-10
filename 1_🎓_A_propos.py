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
    st.header("Qui-suis-je ?")
    left_text, right_image = st.columns((1, 1))
    with left_text:
        subtitle = """<h3> Un étudiant ayant comme but de devenir Data Analyst </h3>"""
        st.markdown(subtitle, unsafe_allow_html=True)
        st.write(""" :wave: Hey ! Je m'appelle Jiek, je suis actuellement étudiant en Data à Hetic. Voici mon Portfolio, vous pourrez y retrouver mes projets, 
        mon parcours scolaire mais également quelque histoire ou photo de mon quotidien !""")
        st.write(""" :computer: Lors de mon BTS SIO en développement web, j'ai eu l'occasion de découvrir le métier de Data Analyst et 
        j'ai vraiment apprécié les différents domaines où il doit être présent, en travaillant avec différentes personnes, à échanger avec plusieurs coeurs de métiers. C'est vraiment un métier que 
        je trouve me correspond, je me suis donc lancé dans l'aventure !
        """)
        st.write(""" :video_game: J'aime bien jouer aux jeux vidéo surtout Teamfight Tactics et aussi tester des restaurants proposant de bons plats maisons :ramen:""")
        st.write(""" :chart_with_upwards_trend: Ce que j'aime dans le travail de Data Analyst : la visualisation de donnée, l'analyse de marché, 
        travailler les données pour les rendre compréhensible par n'importe qui, la prédiction pour aider le client à mieux se développer.""")
        st.write(""" :seedling: Je souhaiterais également avoir la chance de travailler en tant que Product Manager / Data Scientist / BI Analyst""")
        cv_pdf_link = 'Jiek_ruan_data_analyst_cv'
        st.markdown(f"**[Télécharger le CV]({cv_pdf_link})**", unsafe_allow_html=True)
        copyright_footer = """<p>Personnal portfolio for Jiek Ruan &copy 2023</p>"""
        st.markdown(copyright_footer, unsafe_allow_html=True)
    with right_image:
        st.image("logo192x192.png")



