import streamlit as st
import pandas as pd
from api_connector import fetch_match_stats
from predictor import FootballPredictor

st.set_page_config(page_title="IA Predictor Football", page_icon="⚽", layout="wide")

# 1. Dictionnaire des langues
LANGUAGES = {
    "Français": {
        "title": "⚽ IA de Prédiction de Scores de Football",
        "subtitle": "Analyse probabiliste basée sur la Loi de Poisson et Monte-Carlo.",
        "config": "⚙️ Configuration",
        "league": "ID Ligue (Ex: 61 Ligue 1, 39 Premier League)",
        "season": "Saison",
        "home": "Équipe à Domicile",
        "away": "Équipe à l'Extérieur",
        "btn": "🚀 Lancer l'Analyse Probabiliste",
        "lambda_title": "📊 Buts Attendus (λ)",
        "probs_title": "🎯 Probabilités des Marchés (Monte-Carlo)",
        "top_scores": "🏆 Top 5 Scores Exacts les Plus Probables",
        "win_home": "Victoire Domicile",
        "draw": "Match Nul",
        "win_away": "Victoire Extérieur",
    },
    "English": {
        "title": "⚽ Football Score Predictor AI",
        "subtitle": "Probabilistic analysis based on Poisson Law and Monte-Carlo.",
        "config": "⚙️ Settings",
        "league": "League ID (Ex: 61 Ligue 1, 39 Premier League)",
        "season": "Season",
        "home": "Home Team",
        "away": "Away Team",
        "btn": "🚀 Run Probabilistic Analysis",
        "lambda_title": "📊 Expected Goals (λ)",
        "probs_title": "🎯 Market Probabilities (Monte-Carlo)",
        "top_scores": "🏆 Top 5 Most Likely Correct Scores",
        "win_home": "Home Win",
        "draw": "Draw",
        "win_away": "Away Win",
    },
    "Euskara": {
        "title": "⚽ Futbol Puntuazioen Iragarpen Adimen Artifiziala",
        "subtitle": "Poisson-en Legean eta Monte-Carlon oinarritutako analisi probabilistikoa.",
        "config": "⚙️ Ezarpenak",
        "league": "Ligaren IDa (Adib: 61 Ligue 1, 39 Premier League)",
        "season": "Denboraldia",
        "home": "Etxeko Taldea",
        "away": "Kanpoko Taldea",
        "btn": "🚀 Analisi Probabilistikoa Hasi",
        "lambda_title": "📊 Expectatutako Golak (λ)",
        "probs_title": "🎯 Merkatuko Probabilitateak (Monte-Carlo)",
        "top_scores": "🏆 5 Emaitza Zuzenen Probableenak",
        "win_home": "Etxekoen Garaipena",
        "draw": "Berdinketa",
        "win_away": "Kanpokoen Garaipena",
    }
}

# 2. Sélecteur de langue dans la barre latérale
lang_choice = st.sidebar.selectbox("🌐 Hizkuntza / Language / Langue", ["Français", "English", "Euskara"])
t = LANGUAGES[lang_choice]

# 3. Utilisation des textes selon la langue choisie
st.title(t["title"])
st.markdown(t["subtitle"])

st.sidebar.header(t["config"])
league_id = st.sidebar.number_input(t["league"], value=61, step=1)
season = st.sidebar.number_input(t["season"], value=2025, step=1)

col1, col2 = st.columns(2)
with col1:
    home_input = st.text_input(t["home"], value="Paris Saint Germain")
with col2:
    away_input = st.text_input(t["away"], value="Marseille")

if st.button(t["btn"], type="primary"):
    # (Le reste du calcul reste identique...)
    pass
