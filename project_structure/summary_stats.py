import pandas as pd

def compute_summary_statistics():
    df = pd.read_csv('project_original/season-2223_csv.csv')

    quantitative_features = ['HS', 'AS', 'HST']
    qualitative_feature = 'FTR'

    summary_statistics = {}

    for feature in quantitative_features:
        summary_statistics[feature] = {
            'Min': df[feature].min(),
            'Max': df[feature].max(),
            'Median': df[feature].median()
        }

    feature_counts = df[qualitative_feature].value_counts()
    most_frequent_category = feature_counts.idxmax()
    least_frequent_category = feature_counts.idxmin()
    summary_statistics[qualitative_feature] = {
        'Number of Categories': df[qualitative_feature].nunique(),
        'Most Frequent Category': f'{most_frequent_category} ({feature_counts[most_frequent_category]})',
        'Least Frequent Category': f'{least_frequent_category} ({feature_counts[least_frequent_category]})'
    }

    with open('data_processed/summary.txt', 'w') as file:
        for feature, stats in summary_statistics.items():
            file.write(f'{feature}:\n')
            for stat, value in stats.items():
                file.write(f'  {stat}: {value}\n')
            file.write('\n')

    print('Summary statistics saved to data_processed/summary.txt')

compute_summary_statistics()
