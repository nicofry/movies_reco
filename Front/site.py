import streamlit as st
import requests
import pandas as pd
import base64


file_path = "wallpaper.jpg"
with open(file_path, "rb") as f:
    encoded_image = base64.b64encode(f.read()).decode()

page_bg_img = f"""
<style>
[data-testid="stApp"] {{
  background-image: url("data:image/webp;base64,{encoded_image}");
  background-size: cover;
  background-repeat: repeat;
  background-position: center;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Luckiest+Guy&display=swap');

    .simpson-style {
        font-family: 'Luckiest Guy', cursive;
        background-color: lightyellow;
        color: hotpink;
        font-size: 60px;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
    }
    </style>

    <div class="simpson-style">LES SPRINTFIELDS</div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Texte du label */
    label {
        color: hotpink !important;
        font-weight: bold;
    }

    /* Champ input */
    input[type="text"] {
        background-color: white !important;
        color: hotpink !important;
        border: 2px solid hotpink;
        border-radius: 8px;
        padding: 0.5em;
    }

    /* Placeholder (texte grisé initial) */
    input[type="text"]::placeholder {
        color: #ff69b4;
        opacity: 1;
    }
    </style>
""", unsafe_allow_html=True)

query = st.text_input("Tapez un nom de film")
st.markdown("""
    <style>
    /* Import Luckiest Guy font */
    @import url('https://fonts.googleapis.com/css2?family=Luckiest+Guy&display=swap');

    /* Label */
    label {
        color: hotpink !important;
        font-weight: bold;
    }

    input[type="text"] {
        background-color: white !important;
        color: hotpink !important;
        border: 2px solid hotpink;
        border-radius: 8px;
        padding: 0.5em;
    }

    input[type="text"]::placeholder {
        color: #ff69b4;
        opacity: 1;
    }

    /* Selectbox styling */
    .stSelectbox > div[data-baseweb="select"] {
        background-color: white !important;
        border: 2px solid hotpink !important;
        border-radius: 8px !important;
    }

    .stSelectbox .css-1jqq78o-placeholder,
    .stSelectbox .css-1dimb5e-singleValue {
        color: hotpink !important;
        font-weight: bold;
    }

    .css-1n7v3ny-option {
        color: hotpink !important;
        background-color: white !important;
    }

    /* Hotpink message box */
    .hotpink-box {
        background-color: white;
        color: hotpink;
        font-weight: bold;
        padding: 10px;
        border: 2px solid hotpink;
        border-radius: 8px;
        margin-top: 10px;
    }

    /* Button styling */
    div.stButton > button {
        font-family: 'Luckiest Guy', cursive !important;
        font-size: 20px;
        color: hotpink !important;
        background-color: white !important;
        border: 2px solid hotpink !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        margin-right: 10px;
    }

    div.stButton > button:hover {
        background-color: hotpink !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

if query:
    try:
        response = requests.get(f"http://localhost:8000/suggest?name={query}")
        if response.status_code == 200:
            df_titles_json = response.json()
            df_titles = pd.DataFrame(df_titles_json)
            suggestions = df_titles['title_and_year'].to_list()
            
        else:
            st.markdown("<p style='color: hotpink; font-weight: bold;'>There is a couille in the paté</p>", unsafe_allow_html=True)
    except:
        st.markdown("<p style='color: hotpink; font-weight: bold;'>L'API marche po</p>", unsafe_allow_html=True)
    choice = st.selectbox("Choisissez votre film", suggestions)
    if choice:
        st.markdown(f"<p style='color: hotpink; font-weight: bold;'>Tu as choisi {choice}</p>", unsafe_allow_html=True)

        if choice:
            tconst = df_titles[df_titles['title_and_year'] == choice]['tconst'].iloc[0]
            st.markdown("<h4 style='text-align: center;'>Option confort ou option découverte?</h4>", 
            unsafe_allow_html=True)
            # Créer trois colonnes avec espacement pour centrer les boutons
            col1, col2, col3 = st.columns([1, 2, 1])
            
            # Placer les boutons dans la colonne du milieu
            with col2:
                subcol1, subcol2 = st.columns(2)
                with subcol1:
                    launch = st.button('Confort', use_container_width=True)
                with subcol2:
                    launch2 = st.button('Découverte', use_container_width=True)


            if launch or launch2:
                response_reco = requests.get(f"http://localhost:8000/reco?choice={tconst}")
                if response_reco.status_code == 200:
                    recos = response_reco.json()
                    df = pd.DataFrame(recos)
                    base_url = "https://image.tmdb.org/t/p/w500"
                    st.markdown("""
                        <style>
                        .tooltip {
                        position: relative;
                        display: inline-block;
                        }

                        .tooltip .tooltiptext {
                        visibility: hidden;
                        width: 250px;
                        background-color: white;
                        color: hotpink;
                        text-align: left;
                        border-radius: 8px;
                        padding: 10px;
                        border: 2px solid hotpink;
                        position: absolute;
                        z-index: 1;
                        bottom: 110%;
                        left: 50%;
                        margin-left: -125px;
                        opacity: 0;
                        transition: opacity 0.4s;
                        font-size: 14px;
                        }

                        .tooltip:hover .tooltiptext {
                        visibility: visible;
                        opacity: 1;
                        }
                        </style>
                        """, unsafe_allow_html=True)


                    

                    
                if launch:
                        st.markdown("<h5 style='text-align: center;'>Vous allez adorer:</h5>", 
                        unsafe_allow_html=True)
                        cols = st.columns(5)
                        for i, row in enumerate(df.head().itertuples()):  # ou df.tail() selon mode Confort/Découverte
                            with cols[i]:
                                st.markdown(f"""
                                <div class="tooltip">
                                    <img src="{base_url}{row.poster_path}" style="width:100%; border-radius:8px;">
                                    <span class="tooltiptext">{row.overview}</span>
                                </div>
                                <div style="text-align:center;"><strong>{row.primaryTitle}</strong><br>⭐ {round(row.averageRating, 1)}</div>
                                """, unsafe_allow_html=True)



                elif launch2:
                        st.markdown("<h5 style='text-align: center;'>Moins connu mais pourquoi pas:</h5>", 
                        unsafe_allow_html=True)
                        cols = st.columns(5)
                        for i, row in enumerate(df.tail().itertuples()):
                            with cols[i]:
                                st.image(f"{base_url}{row.poster_path}", use_container_width=True)
                                st.markdown(f"**{row.primaryTitle}**<br>⭐ {round(row.averageRating, 1)}", unsafe_allow_html=True)
                else:
                        st.write('There is a couille in the paté')

file_path_gif= "git_donut.gif"
with open(file_path_gif, "rb") as file_:
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
data_url_full = f"data:image/gif;base64,{data_url}"

# Créer trois colonnes pour centrer
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.markdown(
        f"<img src='{data_url_full}' style='width:300px; border-radius:10px;'>",
        unsafe_allow_html=True
    )

