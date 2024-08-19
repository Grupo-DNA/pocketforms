import requests

class TypeformService:
    def __init__(self, token, form_id):
        self.token = token
        self.form_id = form_id
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

    def update_form(self, data):
        url = f'https://api.typeform.com/forms/{self.form_id}'
        response = requests.patch(url, json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()
