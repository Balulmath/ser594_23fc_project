from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score
from time import time
from joblib import dump
import json

def train_classifier(clf, X_train, y_train):
    start = time()
    clf.fit(X_train, y_train)
    end = time()
    print("Model trained in {:2f} seconds".format(end-start))

def predict_labels(clf, features, target):
    start = time()
    y_pred = clf.predict(features)
    end = time()
    print("Made Predictions in {:2f} seconds".format(end-start))
    acc = sum(target == y_pred) / float(len(y_pred))
    return f1_score(target, y_pred, average='micro'), acc

def model(clf, X_train, y_train, X_test, y_test):
    train_classifier(clf, X_train, y_train)
    f1, acc = predict_labels(clf, X_train, y_train)
    print("Training Info:")
    print("-" * 20)
    print("F1 Score:{}".format(f1))
    print("Accuracy:{}".format(acc))
    f1, acc = predict_labels(clf, X_test, y_test)
    print("Test Metrics:")
    print("-" * 20)
    print("F1 Score:{}".format(f1))
    print("Accuracy:{}".format(acc))

def execute_models(X_train, Y_train, X_test, Y_test):
    svc_classifier = SVC(random_state=100, kernel='rbf')
    lr_classifier = LogisticRegression(multi_class='ovr', max_iter=500)
    nbClassifier = GaussianNB()
    dtClassifier = DecisionTreeClassifier()
    rfClassifier = RandomForestClassifier()

    print()
    print("Logistic Regression one vs All Classifier")
    print("-" * 20)
    model(lr_classifier, X_train, Y_train, X_test, Y_test)

    print()
    print("Gaussain Naive Bayes Classifier")
    print("-" * 20)
    model(nbClassifier, X_train, Y_train, X_test, Y_test)

    print()
    print("Random Forest Classifier")
    print("-" * 20)
    model(rfClassifier, X_train, Y_train, X_test, Y_test)

    shouldExport = input('Do you want to export the model(s) (y / n) ? ')
    if shouldExport.strip().lower() == 'y':
        exportedModelsPath = 'exportedModels'
        makedirs(exportedModelsPath, exist_ok=True)
        dump(lr_classifier, f'{exportedModelsPath}/lr_classifier.model')
        dump(nbClassifier, f'{exportedModelsPath}/nb_classifier.model')
        dump(rfClassifier, f'{exportedModelsPath}/rf_classifier.model')

        exportMetaData = dict()
        exportMetaData['home_teams'] = home_encoded_mapping
        exportMetaData['away_teams'] = away_encoded_mapping
        exportMetaDataFile = open(f'{exportedModelsPath}/metaData.json', 'w')
        json.dump(exportMetaData, exportMetaDataFile)
        print(f'Model(s) exported successfully to {exportedModelsPath}/')