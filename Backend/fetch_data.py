import requests

def get_user_id(access_token):
    url = f"https://graph.instagram.com/me?access_token={access_token}&fields=id,username"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def fetch_instagram_data(user_id, access_token):
    url = f"https://graph.instagram.com/{user_id}/media?fields=id,caption&access_token={access_token}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
