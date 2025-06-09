import pandas as pd

def compute_pairwise_correlations():
    df = pd.read_csv('data_original/season-2223_csv.csv')

    selected_features = df[['FTHG', 'FTAG', 'HS']]

    correlation_matrix = selected_features.corr()

    with open('data_processed/correlations.txt', 'w') as file:
        file.write(correlation_matrix.to_string())

compute_pairwise_correlations()
