# main.py

"""
 Serves as the entry point for the application. 
 It may perform initialization tasks, call various setup functions, 
 and ultimately start the application by invoking the server defined 
 in app.py.
"""


from Backend.fetch_data import fetch_data
from Backend.preprocess_data import preprocess_data
from Backend.generate_embeddings import generate_embeddings
from Backend.analyze_mental_health import analyze_mental_health
from Backend.app import app

def main():
    # Example: Fetch, preprocess, and analyze some data
    user_id = "example_user_id"
    api_key = "example_api_key"
    
    data = fetch_data(user_id, api_key)
    preprocessed_data = preprocess_data(data)
    index = generate_embeddings(preprocessed_data)
    analysis_results = analyze_mental_health(index, "signs of mental health issues")
    
    print("Analysis Results:")
    print(analysis_results)
    
    # Run the Flask app
    app.run(debug=True)

if __name__ == '__main__':
    main()
