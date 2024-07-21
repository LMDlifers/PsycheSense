def preprocess_data(data):
    # Extract captions from the Instagram data
    preprocessed_data = [post['caption'] for post in data if 'caption' in post]
    return preprocessed_data
