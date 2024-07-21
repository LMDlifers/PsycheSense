import requests

def get_user_id(access_token):
    url = f"https://graph.instagram.com/me?access_token={access_token}&fields=id,username"
    response = requests.get(url)
    print(f"Request URL for User ID: {url}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def fetch_instagram_data(user_id, access_token):
    url = f"https://graph.instagram.com/{user_id}/media?fields=id,caption&access_token={access_token}"
    print(f"Request URL for Media Data: {url}")
    response = requests.get(url)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == '__main__':
    access_token = "IGQWRPbFlVckNOM1B6MzRndkNxT2ZAUbFYwekY1VnNIanR2WU5rVkIxVzFWeHBUc0dMLTVKZA09iNmliYm5lOVdaT1o2ZAHFRNHpLTGpKNUd3NU52Rm10bWR2UU5IekxUUHRyQ09ZANnhLdXBMc2o5RVcyNUIwSmpLZAGcZD"  # Replace with your access token
    
    # Step 1: Get the user ID
    user_info = get_user_id(access_token)
    if user_info:
        user_id = user_info.get('id')
        print(f"User ID: {user_id}")

        # Step 2: Fetch media data using the user ID
        data = fetch_instagram_data(user_id, access_token)
        print(data)
