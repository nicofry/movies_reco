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


#------------Chargement de la table---------------------------------

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "ML_table.csv")
df = pd.read_csv(file_path)

def normalize(title):
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
    titles_df = df[['tconst','normalized_title','numVotes','title_and_year', 'startYear','popularity']].sort_values(by=['numVotes', 'startYear'], ascending= False)
    list_films = titles_df[titles_df['normalized_title'].apply(lambda x: n_search in(x))]['title_and_year'].to_list()
    return list_films

#------------Préparation de la table au ML--------------------------

X = df.drop(columns=[ 'tconst','primaryTitle', 'genres', 'budget', 'revenue', 'normalized_title', 'poster_path', 'title_and_year', 'overview', 'keywords'])
scaler_nn = StandardScaler()
X_nn_scaled = scaler_nn.fit_transform(X)

#Adaptation de l'importance de l'année de sortie
X_nn_scaled[:,0] = X_nn_scaled[:,0] * 1
#Adaptation de l'importance de la durée du film
X_nn_scaled[:,1] = X_nn_scaled[:,1] * 0.5
#Adaptation de l'importance de la note moyenne
X_nn_scaled[:,2] = X_nn_scaled[:,2] * 2
#Adaptation de l'importance du nombre de votes
X_nn_scaled[:,3] = X_nn_scaled[:,3] * 6
#Adaptation de l'importance de la popularité
X_nn_scaled[:,4] = X_nn_scaled[:,4] * 3
#Adaptation de l'importance du genre
for i in range(5, len(X.columns)):
    X_nn_scaled[:,i] = X_nn_scaled[:,i] * 8

#-----------ML-------------------------------------------------


k = 51017 # Nombre de voisins à trouver (y compris le point lui-même si k>0 et qu'il est dans les données)

nn_model = NearestNeighbors(n_neighbors=k, algorithm='auto', metric='euclidean')
# .fit() indexe les données X_knn_scaled
nn_model.fit(X_nn_scaled) # Entraîner sur les données standardisées X


def ML_lezgo(titre_year:str):
    raw = r"{}".format(titre_year)
    pos = df[df['title_and_year'] == raw].index
    X_test_scaled = X_nn_scaled[pos]

    # Test avec le film
    distances, indices = nn_model.kneighbors(X_test_scaled)
    indices_nn = indices[0][1:6]
    indices_fn = indices[0][-5:]

    n_neighbor_original_indices = X.iloc[indices_nn].index
    f_neighbor_original_indices = X.iloc[indices_fn].index

    # Sélectionner les lignes des voisins dans df et quelques colonnes pertinentes
    nearest_neighbor_info = df.loc[n_neighbor_original_indices][['primaryTitle', 'startYear', 'runtimeMinutes',
    'averageRating','genres', 'poster_path']]
    nearest_neighbor_info['near'] = True
    farest_neighbor_info = df.loc[f_neighbor_original_indices][['primaryTitle', 'startYear', 'runtimeMinutes',
    'averageRating','genres', 'poster_path']]
    farest_neighbor_info['near'] = False

    df_result = pd.concat([nearest_neighbor_info,farest_neighbor_info], axis = 0)


    
    return df_result

