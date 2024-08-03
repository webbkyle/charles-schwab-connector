import requests
import json

class CSConnector:
    base_url = ""

    def __init__(self, username, password):
        self.username = username
        self.password = password
        print(self.username)
        self.auth_token = None
        self.session = requests.Session()
        # self.login()
    
    def login(self):
        login_url = f"{self.base_url}oauth2/token/"
        payload = {
            "username": self.username,
            "password": self.password,
            "grant_type": "password",
            "client_id": "your_client_id",
            "scope": "internal"
        }
        response = self.session.post(login_url, data=payload)
        response_data = response.json()

        if response.status_code == 200 and 'access_token' in response_data:
            self.auth_token = response_data['access_token']
            self.session.headers.update({"Authorization": f"Bearer {self.auth_token}"})
        else:
            raise Exception("Login failed: " + response_data.get('error_description', 'Unknown error'))
        

x = CSConnector('kyle', '123')

print('hello')