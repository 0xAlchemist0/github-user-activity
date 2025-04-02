import requests

base_url = "https://api.github.com"

def make_request(endpoint):
    response = requests.get(base_url + endpoint, headers={"Authorization": "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"})
    if response.status_code == 200:
        return response.json()
    return None
    
    
