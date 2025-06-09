import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
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
precision1 = precision_score(y_val, predictions1, average='weighted')
recall1 = recall_score(y_val, predictions1, average='weighted')

model2 = RandomForestClassifier(n_estimators=150, max_depth=5, random_state=42)
model2.fit(X_train, y_train.values.ravel())
predictions2 = model2.predict(X_val)
accuracy2 = accuracy_score(y_val, predictions2)
f1_score2 = f1_score(y_val, predictions2, average='weighted')
precision2 = precision_score(y_val, predictions2, average='weighted')
recall2 = recall_score(y_val, predictions2, average='weighted')

model3 = RandomForestClassifier(n_estimators=50, max_depth=15, random_state=42)
model3.fit(X_train, y_train.values.ravel())
predictions3 = model3.predict(X_val)
accuracy3 = accuracy_score(y_val, predictions3)
f1_score3 = f1_score(y_val, predictions3, average='weighted')
precision3 = precision_score(y_val, predictions3, average='weighted')
recall3 = recall_score(y_val, predictions3, average='weighted')

os.makedirs('evaluation', exist_ok=True)
with open('evaluation/summary.txt', 'w') as file:
    file.write(
        f'Model 1 - Acc: {accuracy1}, F1: {f1_score1}, ' +
        f'Prec: {precision1}, Rec: {recall1}\n'
    )
    file.write(
        f'Model 2 - Acc: {accuracy2}, F1: {f1_score2}, ' +
        f'Prec: {precision2}, Rec: {recall2}\n'
    )
    file.write(
        f'Model 3 - Acc: {accuracy3}, F1: {f1_score3}, ' +
        f'Prec: {precision3}, Rec: {recall3}\n'
    )

metrics = {
    'Model 1': {'accuracy': accuracy1, 'f1': f1_score1},
    'Model 2': {'accuracy': accuracy2, 'f1': f1_score2},
    'Model 3': {'accuracy': accuracy3, 'f1': f1_score3},
}

labels = list(metrics.keys())
accuracies = [m['accuracy'] for m in metrics.values()]
f1_scores = [m['f1'] for m in metrics.values()]

fig, ax = plt.subplots()
width = 0.35
x = range(len(labels))
ax.bar(x, accuracies, width, label='Accuracy')
ax.bar([p + width for p in x], f1_scores, width, label='F1 Score')

ax.set_ylabel('Score')
ax.set_xticks([p + width/2 for p in x])
ax.set_xticklabels(labels)
ax.legend()

plt.tight_layout()
plt.savefig('evaluation/model_performance.png')
