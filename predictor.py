import numpy as np
from scipy.stats import poisson

class FootballPredictor:
    def __init__(self, home_stats, away_stats):
        self.home_stats = home_stats
        self.away_stats = away_stats

    def calculate_lambdas(self):
        # Calcul des moyennes d'attaque et défense
        lambda_home = (self.home_stats['scored_avg'] + self.away_stats['conceded_avg']) / 2
        lambda_away = (self.away_stats['scored_avg'] + self.home_stats['conceded_avg']) / 2
        return max(lambda_home, 0.2), max(lambda_away, 0.2)

    def predict_probabilities(self, max_goals=5):
        lambda_home, lambda_away = self.calculate_lambdas()
        
        home_probs = [poisson.pmf(i, lambda_home) for i in range(max_goals + 1)]
        away_probs = [poisson.pmf(i, lambda_away) for i in range(max_goals + 1)]
        
        matrix = np.outer(home_probs, away_probs)
        
        prob_home_win = np.sum(np.tril(matrix, -1))
        prob_draw = np.sum(np.diag(matrix))
        prob_away_win = np.sum(np.triu(matrix, 1))
        
        return {
            'home_win': round(prob_home_win * 100, 2),
            'draw': round(prob_draw * 100, 2),
            'away_win': round(prob_away_win * 100, 2),
            'matrix': matrix
        }
