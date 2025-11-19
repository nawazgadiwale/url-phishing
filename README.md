📌 URL Phishing Detection System

A machine-learning based system to detect phishing URLs using lexical feature extraction and a RandomForestClassifier, with a Flask REST API and a Streamlit user interface.

This project is designed for SOC Analyst / Security Engineer portfolios, demonstrating threat detection, ML-based classification, API integration, and UI visualization.

🚀 Features

✔ Machine Learning model (RandomForest) trained on Kaggle phishing dataset
✔ Custom lexical feature extraction (extract_features())
✔ Flask REST API for real-time predictions
✔ Streamlit UI for user-friendly threat checks
✔ Heuristic analysis (URL length, special characters, tokens, subdomains, HTTPS, etc.)
✔ DNS reputation check
✔ Final risk rating: LOW / MEDIUM / HIGH
✔ JSON response with detailed breakdown
✔ Easy to extend with WHOIS / VirusTotal APIs

📂 Project Structure
url-phishing/
│── api/
│   └── app.py                  # Flask API server
│
│── ui/
│   └── streamlit.py            # Streamlit Web UI
│
│── model/
│   ├── phishing_model.pkl      # Trained RandomForest model
│   ├── label_encoder.pkl       # LabelEncoder for label mapping
│   └── feature_engineering.py  # Feature extraction logic
│
│── data/
│   └── urldata.csv             # Kaggle dataset (ignored in git)
│
│── notebook/
│   └── train.ipynb             # Model training notebook
│
│── main.py                     # Optional training script
│── requirements.txt
│── .gitignore
│── README.md

🧠 How It Works

The model uses lexical features only (no URL fetching), making detection safe and fast.
Examples of extracted features:

URL length

Number of dots, slashes, hyphens

Presence of IP address

HTTPS or not

Number of subdomains

Suspicious tokens: login, verify, secure, update

At symbol @

Percent % or encoded characters

These are fed into a RandomForestClassifier, producing high accuracy (> 99%).

The API also performs:

🔹 Heuristic Score

Custom scoring system for suspicious patterns.

🔹 DNS Reputation Check

If a domain doesn't resolve → more suspicious
If URL uses raw IP → also suspicious

🔹 Final Risk Level

HIGH

MEDIUM

LOW

🛠️ Installation
1. Clone the project
git clone https://github.com/yourname/url-phishing.git
cd url-phishing

2. Create virtual environment
python -m venv venv

3. Activate venv

Windows

.\venv\Scripts\Activate

4. Install dependencies
pip install -r requirements.txt

🔥 Running the Application
Start the Flask API
.\venv\Scripts\Activate
python api/app.py


API will run at:

http://localhost:5000/predict

Start Streamlit UI

Open a second terminal:

.\venv\Scripts\Activate
streamlit run ui/streamlit.py


UI will open at:

http://localhost:8501

🧪 Testing the System
✔ Safe URL (benign)
https://www.google.com

❌ Synthetic Phishing URL (safe to test)
http://secure-login-update-google.com.account.verify-user.in/login

❌ IP-Based Suspicious URL
http://103.221.58.9/login/update/account
