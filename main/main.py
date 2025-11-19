import sys
sys.path.append(r"D:\url-phishing")



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

from model.feature_engineering import extract_features

df = pd.read_csv("D:\\url-phishing\\data\\urldata.csv")

# drop column "result" if exists
if "result" in df.columns:
    df = df.drop(columns=["result"])

df.head()

feature_rows = []

for url in df["url"]:
    feature_rows.append(extract_features(url))

X = pd.DataFrame(feature_rows)
y = df["label"]

le = LabelEncoder()
y_encoded = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)


model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)


pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))


os.makedirs("model", exist_ok=True)
joblib.dump(model, r"D:\url-phishing\model\phishing_model.pkl")
joblib.dump(le, r"D:\url-phishing\model\label_encoder.pkl")

print("Model saved successfully!")
