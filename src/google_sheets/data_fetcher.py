class GoogleSheetsDataFetcher:
    def __init__(self, sheets_service, spreadsheet_id, range_name):
        self.sheets_service = sheets_service
        self.spreadsheet_id = spreadsheet_id
        self.range_name = range_name

    def fetch_data(self):
        sheet = self.sheets_service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.spreadsheet_id, range=self.range_name).execute()
        return result.get('values', [])
