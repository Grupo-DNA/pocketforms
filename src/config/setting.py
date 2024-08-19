import json

with open('src/config/secrets.json') as f:
    SECRETS = json.load(f)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = SECRETS['google']['service_account_file']
SPREADSHEET_ID = SECRETS['google']['spreadsheet_id']
SHEET_NAME = SECRETS['google']['sheet_name']
RANGE_NAME = f'{SHEET_NAME}!A1:B'  
