import pandas as pd
from os import path

def gather_data(data_original, season_range):
    data_files = []
    for data_originals in data_original:
        for season in range(season_range[0], season_range[1] + 1):
            data_files.append(
                'data/{}/data/season-{:02d}{:02d}_csv.csv'.format(data_originals, season, season + 1))

    data_frames = []

    for data_file in data_files:
        if path.exists(data_file):
            data_frames.append(pd.read_csv(data_file))

    data = pd.concat(data_frames).reset_index()
    return data
