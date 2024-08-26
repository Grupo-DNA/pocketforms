from typeform.question_creator import TypeformQuestionCreator
from typeform.typeform_service import TypeformService

def group_characteristics_by_trail(data):
    trails = {}
    for row in data:
        trilha, caracteristica = row
        if trilha not in trails:
            trails[trilha] = []
        trails[trilha].append(caracteristica)
    return trails