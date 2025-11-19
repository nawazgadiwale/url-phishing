import streamlit as st
import requests

st.title("🔐 URL Phishing Detection")

url_input = st.text_input("Enter URL")

api_url = "http://localhost:5000/predict"

if st.button("Check URL"):
    res = requests.post(api_url, json={"url": url_input})
    data = res.json()

    if "prediction" in data:
        if data["prediction"].lower() in ["phishing", "malicious"]:
            st.error(f"⚠️ {data['prediction']}")
        else:
            st.success(f"✔️ {data['prediction']}")
    else:
        st.warning("Error: " + str(data))
