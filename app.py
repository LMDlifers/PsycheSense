# app.py

"""
Focuses on setting up and defining the web application or API. 
It contains the core logic for handling HTTP requests and responses.
"""
from Backend.fetch_data import fetch_instagram_data
from Backend.preprocess_data import preprocess_data
from Backend.generate_embeddings import generate_embeddings
from Backend.analyze_mental_health import analyze_mental_health

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json.get('data')
    preprocessed_data = preprocess_data(data)
    index = generate_embeddings(preprocessed_data)
    analysis_results = analyze_mental_health(index, "signs of mental health issues")
    return jsonify(analysis_results)

if __name__ == '__main__':
    app.run(debug=True)
