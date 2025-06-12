# Import bibliothèque de manipulation de dataframe
import pandas as pd
import numpy as np
# Import bibliothèque de gestion de path et texte
import unicodedata
import re
import os
# Import bibliothèque de NLP
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
    # Classer par populartié et date pour faciliter les recherches
    titles_df = df[['tconst','normalized_title','numVotes','title_and_year', 'startYear']].sort_values(by=['numVotes', 'startYear'], ascending= False)
    # Chercher dans les titres normalisés la recherche
    df_titres = titles_df[titles_df['normalized_title'].apply(lambda x: n_search in(x))][['title_and_year', 'tconst']]
    return df_titres

#-----------ML-------------------------------------------------

# Vectorisation de la colonne catégorielle
vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(df['overview_simple'])


def ML_lezgo(tconst:str):
    
    # Récupération de la ligne du film cible
    pos = df[df['tconst'] == tconst].index
    matrix_movie = matrix[pos]
    
    # Recherche des 30 plus proches voisins du film cible
    simil = cosine_similarity(matrix, matrix_movie)
    ind = np.argpartition(simil.ravel(), -30)[-30:]
    neighbor_info = df.loc[ind][['tconst', 'primaryTitle','startYear', 'runtimeMinutes',
   'averageRating', 'numVotes', 'genres', 'poster_path', 'overview']]
    
    # Traitement pour davantage tenir compte des genres
    neighbor_info['genres_list'] = neighbor_info['genres'].apply(lambda x: x.split(','))

        # Création d'une colonne de proximité de genre avec le film cible
    def prox(laliste):
        compteur = 0
        for genre in neighbor_info[neighbor_info['tconst'] == tconst]['genres_list'].values[0]:
            if genre in laliste:
                compteur += 1
        return compteur

    neighbor_info['proxy'] = neighbor_info['genres_list'].apply(prox)
    
    # Exclusion du film cible de la sélection
    neighbor_info = neighbor_info[neighbor_info['tconst'] != tconst]
    

    #Classement par genre/popularité pour augmenter la pertinence
    neighbor_info = neighbor_info.sort_values(by= [ 'proxy','numVotes'], ascending= [False,False])

    # Sélectionner les lignes des résultats pour l'option confort et l'option Découverte
    nearest_neighbor_info = neighbor_info[0:6]
    nearest_neighbor_info['near'] = True
    farest_neighbor_info = neighbor_info[-5:]
    farest_neighbor_info['near'] = False

    df_result = pd.concat([nearest_neighbor_info,farest_neighbor_info], axis = 0)


    
    return df_result