import streamlit as st
import pickle
from feature_extraction import *
import xgboost as xgb

# Load the XGBoost model
loaded_model = xgb.Booster(model_file='model.pickle')

# Load the pre-trained model
# with open('model.pickle', 'rb') as model_file:
#     model = pickle.load(model_file)

def predict_phishing(url):
    features = [
        havingIP(url),
        haveAtSign(url),
        getLength(url),
        getDepth(url),
        redirection(url),
        httpDomain(url),
        tinyURL(url),
        prefixSuffix(url)
    ]
    prediction = model.predict([features])
    return prediction[0]

def main():
    st.title("Phishing URL Detector")

    url_input = st.text_input("Paste the URL to check for phishing:")

    if st.button("Check"):
        if url_input:
            prediction = predict_phishing(url_input)
            if prediction == 1:
                st.error("Phishing Detected! This URL is suspicious.")
            else:
                st.success("No Phishing Detected. This URL is safe.")
        else:
            st.warning("Please paste a URL to check.")

if __name__ == "__main__":
    main()
