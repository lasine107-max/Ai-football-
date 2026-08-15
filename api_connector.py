import requests

def fetch_match_stats(api_key, league_id, season, home_team, away_team):
    url = "https://v3.football.api-sports.io/teams/statistics"
    headers = {'x-apisports-key': api_key}
    
    # Récupération des stats (Exemple basique)
    params_home = {"league": league_id, "season": season, "team": home_team}
    params_away = {"league": league_id, "season": season, "team": away_team}
    
    try:
        res_home = requests.get(url, headers=headers, params=params_home).json()
        res_away = requests.get(url, headers=headers, params=params_away).json()
        
        home_scored = float(res_home['response']['goals']['for']['average']['home'])
        home_conceded = float(res_home['response']['goals']['against']['average']['home'])
        
        away_scored = float(res_away['response']['goals']['for']['average']['away'])
        away_conceded = float(res_away['response']['goals']['against']['average']['away'])
        
        return {
            'home': {'scored_avg': home_scored, 'conceded_avg': home_conceded},
            'away': {'scored_avg': away_scored, 'conceded_avg': away_conceded}
        }
    except Exception as e:
        return None
