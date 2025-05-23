import streamlit as st
import requests
import pandas as pd
import unidecode
import re


st.title("Recherche de films")

query = st.text_input("Tapez un nom de film")

if query:
    try:
        response = requests.get(f"http://localhost:8000/suggest?name={query}")
        if response.status_code == 200:
            suggestions = response.json()
        else:
            st.write('There is a couille in the paté')
    except:
        st.write("L'API marche po")

    choice = st.selectbox("Choisissez votre film",suggestions)
    if choice:
        st.write(f'Tu as choisi {choice}')

