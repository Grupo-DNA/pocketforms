import requests
from typeform.question_creator import TypeformQuestionCreator

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
		response = requests.put(url, json=data, headers=self.headers)
		
		try:
			response.raise_for_status()
		except requests.exceptions.HTTPError as e:
			print(f'HTTPError: {e}')
			print(f'Status Code: {response.status_code}')
			print(f'Response Body: {response.text}')
			raise

		return response.json()
	
	def get_form(self):
		url = f'https://api.typeform.com/forms/{self.form_id}'
		response = requests.get(url, headers=self.headers)
		
		try:
			response.raise_for_status()
		except requests.exceptions.HTTPError as e:
			print(f'HTTPError: {e}')
			print(f'Status Code: {response.status_code}')
			print(f'Response Body: {response.text}')
			raise

		return response.json()
	
	def update_form_with_new_questions(self,typeform_service, trilhas_caracteristicas):
		typeformcreator = TypeformQuestionCreator
		existing_form = typeform_service.get_form()		
		new_questions = typeformcreator.create_questions_data(trilhas_caracteristicas)
		existing_form['fields'].extend(new_questions)
		response = typeform_service.update_form(existing_form)

		if response.get('status_code') == 200:
			print("Formulário atualizado com sucesso!")
			#print(response.json())
		else:
			print(f"Erro ao atualizar o formulário: {response}")
