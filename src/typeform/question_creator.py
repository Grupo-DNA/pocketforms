class TypeformQuestionCreator:
	def __init__(self, typeform_service):
		self.typeform_service = typeform_service

	def create_question(self, trilha, caracteristicas):
		# Cria uma nova questão de múltipla escolha e a adiciona ao formulário
		data = [
			{
				"op": "add",  # ou "replace" se for atualizar uma questão existente
				"path": "/fields",
				"value": {
					"title": f'Escolha até 10 características para a trilha: {trilha}',
					"type": "multiple_choice",
					"properties": {
						"choices": [{"label": caracteristica} for caracteristica in caracteristicas],
						"allow_multiple_selections": True,
						"randomize": False,
						"vertical_alignment": True
					},
					"validations": {
						"required": False,
						"max_choices": 10
					}
				}
			}
		]
		
		print(data)
		return self.typeform_service.update_form(data)

