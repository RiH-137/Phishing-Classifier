from flask import Flask, request, jsonify
from feature_extraction import havingIP, haveAtSign, getLength, getDepth, redirection, httpDomain, tinyURL, prefixSuffix


from feature_extraction import *


app = Flask(__name__)

@app.route('/', methods=['POST'])
def extract_features():
    try:
        url = request.json['url']
        features = feature_Extraction(url)
        result = dict(zip(feature_names[:-1], features))  # Exclude 'Label' from result
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
