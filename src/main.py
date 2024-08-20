from google_sheets.sheet_service import get_sheets_service
from google_sheets.data_fetcher import GoogleSheetsDataFetcher
from typeform.typeform_service import TypeformService
from typeform.question_creator import TypeformQuestionCreator
from config.setting import SCOPES, SERVICE_ACCOUNT_FILE, SPREADSHEET_ID, RANGE_NAME, TYPEFORM_TOKEN, TYPEFORM_FORM_ID
from utils import group_characteristics_by_trail

def main():
    sheets_service = get_sheets_service(SERVICE_ACCOUNT_FILE, SCOPES)
    data_fetcher = GoogleSheetsDataFetcher(sheets_service, SPREADSHEET_ID, RANGE_NAME)
    data = data_fetcher.fetch_data()

    trails = group_characteristics_by_trail(data)

    typeform_service = TypeformService(TYPEFORM_TOKEN, TYPEFORM_FORM_ID)
    question_creator = TypeformQuestionCreator(typeform_service)

    for trilha, caracteristicas in trails.items():
        print('trilha',trilha,'caracteristicas',caracteristicas)
        question_creator.create_question(trilha, caracteristicas)

if __name__ == "__main__":
    main()
