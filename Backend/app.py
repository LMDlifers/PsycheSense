from flask import Flask, request, jsonify
from preprocess_data import preprocess_data
from fetch_data import get_user_id, fetch_instagram_data
from generate_embeddings import generate_embeddings
from analyze_mental_health import analyze_mental_health

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    access_token = request.json.get('access_token')
    user_info = get_user_id(access_token)
    if user_info:
        user_id = user_info.get('id')
        media_data = fetch_instagram_data(user_id, access_token)
        if media_data:
            media_posts = media_data.get('data', [])
            preprocessed_data = preprocess_data(media_posts)
            embeddings = generate_embeddings(preprocessed_data)
            analysis_results = analyze_mental_health(embeddings)
            return jsonify(analysis_results)
    return jsonify({"error": "Failed to analyze data."})

if __name__ == '__main__':
    app.run(debug=True)
