---------------------movies_reco---------------------------

Table des matières:

1. Installation
2. Composition
3. Utilisation
4. Credits

------------------------------------------------------------

1. INSTALLATION

Tout simplement télécharger (ou faire un gitclone) depuis GitHub.
Toutes les bibliothèques utilisées sont dans requirements.txt à la racine du projet.

-------------------------------------------------------------

2. COMPOSITION

📂 Dossier Dataset :  

__init__.py : Permet la relation inter-dossier  

back.py : Contient les différentes fonctions de recommandation  

main.py : Contient l'API  

NLP_table_prep.csv : Table de données utilisée pour les recommandations (voir plus bas)  

📂 Dossier Front :  

__init__.py : Permet la relation inter-dossier  

site.py : Interface utilisateur avec Streamlit  

wallpaper.jpg : Image de fond du site  

git_donut.gif : Gif affiché sur la page front  

 Fichiers à la racine :  
 
requirements.txt : Liste des bibliothèques utilisées  

readme.txt : C'est ici !  

 Focus sur NLP_table_prep.csv :  
 
Taille : 51 467 lignes × 18 colonnes  

Colonnes principales :  

Colonne	Description  

Unnamed: 0	Numéro de ligne  

primaryTitle	Titre du film (version française)  

tconst	Identifiant IMDB  

runtimeMinutes	Durée du film (minutes)  

genres	Genres du film (max 3)  

averageRating	Note moyenne IMDB  

overview	Résumé du film (en anglais)  

poster_path	Lien (partiel) vers le poster (depuis AlloCiné)  

title_and_year	Titre + année (utile pour différencier les remakes)  

nconst	Identifiants IMDB des acteurs et du réalisateur  

all_categ	Concaténation de genres, overview, acteurs, keywords, Bonfilm  

overview_simple	Résultat de all_categ passé dans un normalizer + lemmatiseur  

startYear	Année de sortie  

normalized_title	Version normalisée de primaryTitle  

numVotes	Nombre de votes IMDB  

keywords	Mots-clés associés (depuis TMDB)  

### 📊 Colonnes principales

| Colonne            | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `Unnamed: 0`        | Numéro de ligne                                                             |
| `primaryTitle`      | Titre du film (version française)                                           |
| `tconst`            | Identifiant IMDB                                                            |
| `runtimeMinutes`    | Durée du film (minutes)                                                     |
| `genres`            | Genres du film (max 3)                                                      |
| `averageRating`     | Note moyenne IMDB                                                           |
| `overview`          | Résumé du film (en anglais)                                                 |
| `poster_path`       | Lien (partiel) vers le poster (depuis AlloCiné)                             |
| `title_and_year`    | Titre + année (utile pour différencier les remakes)                         |
| `nconst`            | Identifiants IMDB des acteurs et du réalisateur                             |
| `all_categ`         | Concaténation de genres, overview, acteurs, keywords, Bonfilm               |
| `overview_simple`   | Résultat de `all_categ` passé dans un normalizer + lemmatiseur              |
| `startYear`         | Année de sortie                                                             |
| `normalized_title`  | Version normalisée de `primaryTitle`                                        |
| `numVotes`          | Nombre de votes IMDB                                                        |
| `keywords`          | Mots-clés associés (depuis TMDB)                                            |


Connu	Popularité NLP :  

   - filmconnu si numVotes > 7000	  
   
   - sinon filmpasconnu	  
   
Bonfilm	Qualité NLP :  

   - Topfilm si averageRating > 8	  
   
   - Boffilm si > 5	  
   
   - Nazefilm si > 3	  
   
   - Epicnanar sinon	  
   
📌 Filtrage initial :  

Films sortis entre 1960 et 2025, et diffusés en France uniquement.

-------------------------------------------------------------

3. UTILISATION.

1/ Charger l'ensemble du projet.  

2/ Ouvrir le fichier back.py avec VScode ou un autre IDE.  

3/ Dans l'invite de commande, taper (sous BASH): uvicorn main:app --reload   

Ca va lancer l'API (Attention! il faut bien être dans le dossier Dataset sur BASH!).  

4/ Ouvrir une nouvelle invite de commande et se déplacer dans le dossier Front  

5/ Taper streamlit run site.py  


---Dans le navigateur---

1/ Taper un nom de film ou fragment de nom de film (les titres sont les titres français!)  

2/ Cliquer et choisir dans la liste déroulante le film désiré  

3/ Cliquer sur option Confort ou Découverte.  


Voilà!

-------------------------------------------------------------

4. CREDITS

Merci à tous, la promo Wild 2025, Viven, Abdel, la boulangerie du coin et ses flans.
Merci à vous, vous êtes incroyables!


![Movie Suggestions](https://raw.githubusercontent.com/nicofry/movies_reco/main/Screenshot%202025-06-12%20at%2016.40.41.png?raw=true)





