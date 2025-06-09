import os
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    ConfusionMatrixDisplay,
)
import matplotlib.pyplot as plt

test_data = pd.read_csv('data_processed/X_test.csv')

if 'Date' in test_data.columns:
    date_format = '%m/%d/%y'  # Specify the date format here
    test_data['Date'] = pd.to_datetime(test_data['Date'], format=date_format, errors='coerce')
    test_data['Year'] = test_data['Date'].dt.year
    test_data['Month'] = test_data['Date'].dt.month
    test_data['Day'] = test_data['Date'].dt.day
    test_data.drop('Date', axis=1, inplace=True)

categorical_cols = test_data.select_dtypes(include=['object']).columns
for col in categorical_cols:
    le = LabelEncoder()
    test_data[col] = le.fit_transform(test_data[col].astype(str))

imputer = SimpleImputer(strategy='mean')
test_data_imputed = imputer.fit_transform(test_data)

model = joblib.load('models/random_forest_model.pkl')
predictions = model.predict(test_data_imputed)

pd.DataFrame({'prediction': predictions}).to_csv('data_processed/predictions.csv', index=False)
print('Predictions saved to data_processed/predictions.csv')

# evaluate prediction metrics using the test labels
true_labels = pd.read_csv('data_processed/y_test.csv')['FTR']
accuracy = accuracy_score(true_labels, predictions)
precision = precision_score(true_labels, predictions, average='weighted')
recall = recall_score(true_labels, predictions, average='weighted')
f1 = f1_score(true_labels, predictions, average='weighted')

report = classification_report(true_labels, predictions)
cm_display = ConfusionMatrixDisplay.from_predictions(true_labels, predictions)
plt.tight_layout()
plt.savefig('evaluation/confusion_matrix.png')
plt.close()

os.makedirs('evaluation', exist_ok=True)
with open('evaluation/prediction_metrics.txt', 'w') as file:
    file.write(f'Accuracy: {accuracy}\n')
    file.write(f'Precision: {precision}\n')
    file.write(f'Recall: {recall}\n')
    file.write(f'F1 Score: {f1}\n')
    file.write('\nClassification Report:\n')
    file.write(report)

with open('evaluation/prediction_accuracy.txt', 'w') as acc_file:
    acc_file.write(str(accuracy))

print(f'Prediction accuracy: {accuracy}')
