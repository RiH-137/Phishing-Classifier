from flask import Flask, request, jsonify
import requests
import streamlit as st

from URLFeatureExtraction import featureExtraction,feature_names

app = Flask(__name__)

@app.route('/', methods=['POST'])
def extract_features():
    try:
        url = request.json['url']
        features = featureExtraction(url)
        result = dict(zip(feature_names[:-1], features))  # Exclude 'Label' from result
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Streamlit code
    st.title('URL Feature Extractor')

    url_input = st.text_input('Enter URL:')
    if st.button('Extract Features'):
        if url_input:
            st.info('Extracting features...')
            try:
                response = requests.post('/', json={'url': url_input})
                if response.status_code == 200:
                    features = response.json()
                    if 'error' in features:
                        st.error(features['error'])
                    else:
                        st.success('Features extracted successfully!')
                        st.write(features)
                else:
                    st.error('Unable to fetch features')
            except Exception as e:
                st.error(f'Error: {e}')
        else:
            st.warning('Please enter a URL to extract features.')

    app.run(debug=True)











    