from flask import Flask, request, jsonify
import joblib
import pandas as pd
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from model.feature_engineering import extract_features

MODEL_PATH = r"D:\url-phishing\model\phishing_model.pkl"
ENCODER_PATH = r"D:\url-phishing\model\label_encoder.pkl"

model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if "url" not in data:
        return jsonify({"error": "URL not provided"}), 400

    url = data["url"]
    features = pd.DataFrame([extract_features(url)])
    prediction = model.predict(features)[0]
    label = encoder.inverse_transform([prediction])[0]

    return jsonify({"url": url, "prediction": label})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(port=5000)
