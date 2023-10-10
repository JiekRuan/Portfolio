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
    st.header("Projects")
    with st.container():
        left_text, right_image = st.columns((2,1))
        with left_text:
            st.subheader("Business Analytics - Analyse des utilisateurs Netflix")
            st.write("Projet personnel BI")
            st.write("Compétences : Power Bi")
            skills_list = """<ul>
                <li>Dashboard intéractif sur les utilisateurs Netflix</li>
                <li>Nettoyage et formatage des données notamment la date</li>
                <li>Visuel adaptatif par rapport à: l'âge, le sexe, le type de l'appareil et type de l'abonnement</li>
                <li>Affichage des informations comme le nombre de nouveaux utilisateurs par mois et la répartition des utilisateurs par pays</li>
            </ul>"""
            github_link = '[Voir sur GitHub](https://github.com/JiekRuan/Netflix_analytics_Bi)'
            st.markdown(skills_list,unsafe_allow_html=True)
            st.markdown(github_link,unsafe_allow_html=True)
        with right_image:
            st.image("./images/Netflix.png")
    with st.container():
        left_text, right_image = st.columns((2,1))
        with left_text:
            st.subheader("Machine learning - prédiction sur des voyageurs")
            st.write("Projet python Bachelor Hetic")
            st.write("Compétences : Python - Pandas - Matplotlib - Numpy - Seaborn - Sklearn")
            skills_list = """<ul>
                <li>Préparation des données puis nous avons procédé à la : Normalisation / Entrainement / Teste</li>
                <li>Le model de prédiction utilisé est la régression lineaire</li>
                <li>Le résultat final est le résultat avec la meilleure MSE</li>
                <li>Comparaison à la fin entre la vérité terrain et la prédiction obtenue par le model</li>
            </ul>"""
            github_link = '[Voir sur GitHub](https://github.com/JiekRuan/Travelers-Forecasting)'
            st.markdown(skills_list,unsafe_allow_html=True)
            st.markdown(github_link,unsafe_allow_html=True)
        with right_image:
            st.image("./images/travelers_forecast.png")
    with st.container():
        left_text, right_image = st.columns((2,1))
        with left_text:
            st.subheader("Data Analyst - EDA de jeu vidéo")
            st.write("Projet personnel analyse de donnée")
            st.write("Compétences : Python - Pandas - Matplotlib - Seaborn - Scipy")
            skills_list = """<ul>
                <li>Nettoyage des données en retirant les valeurs nulles</li>
                <li>S'intéresser à l'année où il y a eu le plus de vente en triant les valeurs</li>
                <li>Regarder l'année avec le plus de vente de jeu dans le monde</li>
                <li>Regarder les ventes par genre, editeur et console</li>
                <li>Types de graphiques utilisés : Bar chart / Line chart</li>
            </ul>"""
            github_link = '[Voir sur GitHub](https://github.com/JiekRuan/EDA_games_sales)'
            st.markdown(skills_list,unsafe_allow_html=True)
            st.markdown(github_link,unsafe_allow_html=True)
        with right_image:
            st.image("./images/games_sales.png")
    with st.container():
        left_text, right_image = st.columns((2,1))
        with left_text:
            st.subheader("Application d'entrainement de tir FPS")
            st.write("Projet personnel python")
            st.write("Compétences : Python - Pygame")
            skills_list = """<ul>
                <li>Cliquez sur des cibles qui apparaissent à intervalle régulié pour monter votre le score</li>
                <li>Comptage du nombre de cible, votre temps ainsi que le nombre de vie restant à la fin</li>
                <li>GUI python en utilisant pygame</li>
            </ul>"""
            github_link = '[Voir sur GitHub](https://github.com/JiekRuan/python-aim-app)'
            st.markdown(skills_list,unsafe_allow_html=True)
            st.markdown(github_link,unsafe_allow_html=True)
        with right_image:
            st.image("./images/aim_app.png")
    with st.container():
        left_text, right_image = st.columns((2,1))
        with left_text:
            st.subheader("Clone de l'interface de Instagram 2021")
            st.write("Projet de clonage Front-End de l'application Instagram BTS SIO")
            st.write("Compétences : HTML - CSS - JavaScript")
            skills_list = """<ul>
                <li></li>
                <li></li>
                <li></li>
            </ul>"""
            github_link = '[Voir sur GitHub](https://github.com/JiekRuan/tp_instagram2021)'
            st.markdown(github_link,unsafe_allow_html=True)
        with right_image:
            st.image("./images/instagram.png")
    with st.container():
        left_text, right_image = st.columns((2,1))
        with left_text:
            st.subheader("Clone de l'interface de recherche Google")
            st.write("Premier petit projet web de mon BTS SIO")
            st.write("Compétences : HTML - CSS")
            skills_list = """<ul>
                <li></li>
                <li></li>
                <li></li>
            </ul>"""
            github_link = '[Voir sur GitHub](https://github.com/JiekRuan/TP_Clone_Google)'
            st.markdown(github_link,unsafe_allow_html=True)
        with right_image:
            st.image("./images/google.png")
copyright_footer = """<p>Personnal portfolio for Jiek Ruan &copy 2023</p>"""
st.markdown(copyright_footer, unsafe_allow_html=True)