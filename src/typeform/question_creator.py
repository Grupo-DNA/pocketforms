class TypeformQuestionCreator:
	def __init__(self, typeform_service):
		self.typeform_service = typeform_service

	@staticmethod
	def create_questions_data(trilhas_caracteristicas):
		new_fields = []
	
		for trilha, caracteristicas in trilhas_caracteristicas.items():
			question = {
				"title": f"Escolha características para a trilha: deuc erto? {trilha}",
				"type": "multiple_choice",
				"properties": {
					"choices": [{"label": caracteristica} for caracteristica in caracteristicas],
					"allow_multiple_selection": True,
					"randomize": False,
					"vertical_alignment": True
				},
				"validations": {
					"required": False
				}
			}
			new_fields.append(question)
	
		return new_fields
