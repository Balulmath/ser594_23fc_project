import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

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
