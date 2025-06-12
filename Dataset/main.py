from fastapi import FastAPI
# Import des bibliothèques et fonctions nécessaires
import pandas as pd
from back import ML_lezgo,title_list, normalize
import os

app = FastAPI()
# Commande de lancement: uvicorn main:app --reload

# Renvoi de liste de titres en prenant le résultat de la recherche
@app.get('/suggest')
def suggest(name:str):
    df_titles = title_list(name).to_dict()
    return df_titles

# Renvoi des résultats du ML sur le cible cible
@app.get('/reco')
def reco(choice:str):
    df_result = ML_lezgo(choice).to_dict()
    return df_result