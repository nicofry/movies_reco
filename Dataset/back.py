# Import bibliothèque de manipulation de dataframe
import pandas as pd
import numpy as np
from datetime import datetime
# Import split data
from sklearn.model_selection import train_test_split
# Import modèle de ML NON Supervisé
from sklearn.neighbors import NearestNeighbors
# Import outil standardisation de la donnée
from sklearn.preprocessing import StandardScaler
# Import pipeline
from sklearn.pipeline import Pipeline
import unidecode
import unicodedata
import re
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#------------Chargement de la table---------------------------------

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, r"NLP_table_prep.csv")
df = pd.read_csv(file_path)

def normalize(title:str):
    # Mettre en minuscules et enlever les espaces superflus
    title = title.strip().lower()
    # Enlever les accents
    title = unicodedata.normalize('NFD', title)
    title = title.encode('ascii', 'ignore').decode("utf-8")
    # Enlever la ponctuation
    title = re.sub(r'[^\w\s]', '', title)
    return title


def title_list(search:str):
    n_search = normalize(search)
    titles_df = df[['tconst','normalized_title','numVotes','title_and_year', 'startYear']].sort_values(by=['numVotes', 'startYear'], ascending= False)
    df_titres = titles_df[titles_df['normalized_title'].apply(lambda x: n_search in(x))][['title_and_year', 'tconst']]
    return df_titres

#-----------ML-------------------------------------------------


vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(df['all_categ'])


def ML_lezgo(tconst:str):
    

    
    pos = df[df['tconst'] == tconst].index
    matrix_movie = matrix[pos]
    simil = cosine_similarity(matrix, matrix_movie)

    # Test avec le film
    ind = np.argpartition(simil.ravel(), -30)[-30:]


    neighbor_info = df.loc[ind][['tconst', 'primaryTitle','startYear', 'runtimeMinutes',
   'averageRating', 'numVotes', 'genres', 'poster_path']]
    
    neighbor_info['genres_list'] = neighbor_info['genres'].apply(lambda x: x.split(','))

    def prox(laliste):
        compteur = 0
        for genre in neighbor_info[neighbor_info['tconst'] == tconst]['genres_list'].values[0]:
            if genre in laliste:
                compteur += 1
        return compteur

    neighbor_info['proxy'] = neighbor_info['genres_list'].apply(prox)
    neighbor_info = neighbor_info[neighbor_info['tconst'] != tconst]
    


    neighbor_info = neighbor_info.sort_values(by= [ 'proxy','numVotes'], ascending= [False,False])

    # Sélectionner les lignes des voisins dans df et quelques colonnes pertinentes
    nearest_neighbor_info = neighbor_info[0:6]
    nearest_neighbor_info['near'] = True
    farest_neighbor_info = neighbor_info[-5:]
    farest_neighbor_info['near'] = False

    df_result = pd.concat([nearest_neighbor_info,farest_neighbor_info], axis = 0)


    
    return df_result