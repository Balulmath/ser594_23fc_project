import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
import joblib
import os

X = pd.read_csv('data_processed/X_train.csv')
y = pd.read_csv('data_processed/y_train.csv')

if 'Date' in X.columns:
    X['Date'] = pd.to_datetime(X['Date'], errors='coerce')
    X['Year'] = X['Date'].dt.year
    X['Month'] = X['Date'].dt.month
    X['Day'] = X['Date'].dt.day
    X.drop('Date', axis=1, inplace=True)

categorical_cols = X.select_dtypes(include=['object']).columns
for col in categorical_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))

imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

model1 = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
model1.fit(X_train, y_train.values.ravel())
predictions1 = model1.predict(X_val)
accuracy1 = accuracy_score(y_val, predictions1)
f1_score1 = f1_score(y_val, predictions1, average='weighted')

model2 = RandomForestClassifier(n_estimators=150, max_depth=5, random_state=42)
model2.fit(X_train, y_train.values.ravel())
predictions2 = model2.predict(X_val)
accuracy2 = accuracy_score(y_val, predictions2)
f1_score2 = f1_score(y_val, predictions2, average='weighted')

model3 = RandomForestClassifier(n_estimators=50, max_depth=15, random_state=42)
model3.fit(X_train, y_train.values.ravel())
predictions3 = model3.predict(X_val)
accuracy3 = accuracy_score(y_val, predictions3)
f1_score3 = f1_score(y_val, predictions3, average='weighted')

os.makedirs('evaluation', exist_ok=True)
with open('evaluation/summary.txt', 'w') as file:
    file.write(f'Model 1 - Accuracy: {accuracy1}, F1 Score: {f1_score1}\n')
    file.write(f'Model 2 - Accuracy: {accuracy2}, F1 Score: {f1_score2}\n')
    file.write(f'Model 3 - Accuracy: {accuracy3}, F1 Score: {f1_score3}\n')
