from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def get_sheets_service(service_account_file, scopes):
    creds = Credentials.from_service_account_file(service_account_file, scopes=scopes)
    return build('sheets', 'v4', credentials=creds)
