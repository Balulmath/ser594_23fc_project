from sklearn.preprocessing import LabelEncoder
import pandas as pd

def preprocess_data(data):
    encoder = LabelEncoder()
    home_encoded = encoder.fit_transform(data['HomeTeam'])
    home_encoded_mapping = dict(
        zip(encoder.classes_, encoder.transform(encoder.classes_).tolist()))
    data['home_encoded'] = home_encoded

    encoder = LabelEncoder()
    away_encoded = encoder.fit_transform(data['AwayTeam'])
    away_encoded_mapping = dict(
        zip(encoder.classes_, encoder.transform(encoder.classes_).tolist()))
    data['away_encoded'] = away_encoded

    input_filter = ['home_encoded', 'away_encoded', 'HTHG', 'HTAG', 'HS',
                    'AS', 'HST', 'AST', 'HR', 'AR']
    output_filter = ['FTR']
    cols_to_consider = input_filter + output_filter
    data = data[cols_to_consider]
    data = data.dropna(axis=0)
    return data, home_encoded_mapping, away_encoded_mapping, input_filter, output_filter
