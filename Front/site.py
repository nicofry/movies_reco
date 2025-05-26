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

        if choice:
            st.write('Option confort ou option découverte?')
            launch = st.button('Confort')
            launch2 = st.button('Découverte')
            if launch or launch2:
                response_reco = requests.get(f"http://localhost:8000/reco?choice={choice}")
                if response_reco.status_code == 200:
                    recos = response_reco.json()
                    df = pd.DataFrame(recos)
                    if launch:
                        st.write('Vous allez adorer:')
                        st.dataframe(df.head())
                    elif launch2:
                        st.write('A vos antipodes, vous trouverez:')
                        st.dataframe(df.tail())
                else:
                    st.write('There is a couille in the paté')

