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

# user_email = st.text_input("Votre adresse e-mail")
# subject = st.text_input("Sujet du message")
# message = st.text_area("Message")

# def send_email(user_email, subject, message):
#     smtp_server = "smtp.gmail.com"
#     smtp_port = 587
#     smtp_username = "votre_adresse@gmail.com"
#     smtp_password = "votre_mot_de_passe"

#     msg = EmailMessage()
#     msg["From"] = user_email
#     msg["To"] = "jiekruan@gmail.com"
#     msg["Subject"] = subject
#     msg.set_content(message)

#     try:
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()
#         server.login(smtp_username, smtp_password)

#         server.send_message(msg)

#         st.success("Votre e-mail a été envoyé avec succès!")
#     except Exception as e:
#         st.error(f"Une erreur s'est produite lors de l'envoi de l'e-mail : {e}")
#     finally:
#         server.quit()

# if st.button("Envoyer"):
#     if user_email and subject and message:
#         send_email(user_email, subject, message)
#     else:
#         st.warning("Veuillez remplir tous les champs du formulaire.")

st.write("Vous pouvez également vous connectez avec sur moi différent réseaux :")

with st.container():
    left, right = st.columns((1,6))
    with left:
        st.image("./images/Linkedin.png")
    with right:
        st.image("./images/Github.png")

copyright_footer = """<p>Personnal portfolio for Jiek Ruan &copy 2023</p>"""
st.markdown(copyright_footer, unsafe_allow_html=True)