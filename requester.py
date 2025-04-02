import requests

base_url = "https://api.github.com"

def make_request(endpoint):
    response = requests.get(base_url + endpoint, headers={"Authorization": ""})
    if response.status_code == 200:
        return response.json()
    return None
    
    
