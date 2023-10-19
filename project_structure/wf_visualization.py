import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_plots():
    if not os.path.exists('visuals'):
        os.makedirs('visuals')

    df = pd.read_csv('data_original/season-2223_csv.csv')

    quantitative_features = ['FTHG', 'FTAG', 'HTHG']

    for i in range(len(quantitative_features)):
        for j in range(i+1, len(quantitative_features)):
            plt.figure()
            plt.scatter(df[quantitative_features[i]], df[quantitative_features[j]])
            plt.xlabel(quantitative_features[i])
            plt.ylabel(quantitative_features[j])
            plt.title(f'Scatter plot of {quantitative_features[i]} and {quantitative_features[j]}')
            plt.savefig(f'visuals/scatter_{quantitative_features[i]}_{quantitative_features[j]}.png')

    qualitative_features = ['FTR']  

    for feature in qualitative_features:
        plt.figure()
        sns.histplot(data=df, x=feature, kde=True) 
        plt.title(f'Histogram of {feature}')
        plt.savefig(f'visuals/histogram_{feature}.png')

create_plots()
