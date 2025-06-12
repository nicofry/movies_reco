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

Dossier Dataset:
	- __init__.py:    Permet la relation interdossier
	- back.py:    Fichier python contenant les différentes fonctions permettant la recommandation.
	- main.py:    Fichier python contenant l'API.
	- NLP_table_prep.csv:    Table de données dont sont issues les informations de recommandation (composition plus loin).
Dossier Front:
	- __init__.py:    Permet la relation interdossier.
	- site.py:    Fichier python contenant l'interface Streamlit.
	- wallpaper.jpg:    Image de fond du site.
	- git_donut.gif:    Gif sur le front.

requirements.txt:    Liste des bibliothèques utilisées.
readme.txt:    C'est là!

(Focus sur NLP_table_prep:
CSV de 51467 lignes et 18 colonnes
Colonnes:-"Unnamed: 0":    Numéro de ligne
	 -"primaryTitle":    Titre du film dans sa version française
	 -"tconst":    identifiant IMDB du film
	 -"runtimeMinutes":    durée en minutes du film
	 -"genres":    étiquettes de genre attribuées au film (3 maximum)
	 -"averageRating":    Note moyenne sur IMDB
	 -"overview":    Résumé du film (en anglais)
	 -"poster_path":    Fragment de lien vers le poster depuis allocine
	 -"title_and_year":    Concaténation des titres et années (pour retrouver en cas de remake)
	 -"nconst":    Identifiants IMDB des acteurs présents du film et du director.
	 -"all_categ":    Concatenation de genres, overview, nconst, keywords, Bonfilm.
	 -"overview_simple":    résultat de la colonne all_categ passée dans un normalizer et lemma (dans back.py)
	 -"startYear":    Année de sortie
	 -"normalized_title":    Version normalisée de primaryTitle (passée dans la fonction de back.py prévue à cet effet).
	 -"numVotes":    Nombre de votes sur IMDB
	 -"keywords":    Mots clés associés au film (depuis TMDB)
	 -"Connu":    Métrique de popularité pour le NLP. Si numVotes > 7000 classé 'filmconnu'. Sinon 'filmpasconnu'
	 -"Bonfilm":    Métrique de note du film pour le NLP¨. Si averageRating > 8: 'Topfilm'. Sinon si > 5: 'Boffilm'. Sinon si > 3: "Nazefilm". Sinon "Epicnanar".

Les lignes sont les films, la sélection s'est fait sur un filtre des films de 1960 à 2025 et uniquement ceux sortis en France.)


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


<p align="center">
  <img src="https://raw.githubusercontent.com/nicofry/movies_reco/main/Screenshot%202025-06-12%20at%2016.40.41.png" width="600"/>
</p>




