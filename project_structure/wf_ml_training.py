import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Load the data
X_train = pd.read_csv('data_processed/X_train.csv')
y_train = pd.read_csv('data_processed/y_train.csv')

# Handle date columns
if 'Date' in X_train.columns:
    X_train['Date'] = pd.to_datetime(X_train['Date'], errors='coerce')
    X_train['Year'] = X_train['Date'].dt.year
    X_train['Month'] = X_train['Date'].dt.month
    X_train['Day'] = X_train['Date'].dt.day
    X_train.drop('Date', axis=1, inplace=True)

# Encode categorical columns
categorical_cols = X_train.select_dtypes(include=['object']).columns
for col in categorical_cols:
    le = LabelEncoder()
    X_train[col] = le.fit_transform(X_train[col].astype(str))

# Impute missing values
imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train)

# Train the RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train_imputed, y_train.values.ravel())

# Save the trained model
models_path = 'models/'
os.makedirs(models_path, exist_ok=True)
joblib.dump(model, os.path.join(models_path, 'random_forest_model.pkl'))
