import gspread
from oauth2client.service_account import ServiceAccountCredentials

def search(model:str = None):
    # Определяем область доступа
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]

    # Загружаем ключ сервисного аккаунта
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    # Открываем таблицу по названию
    sheet = client.open("Transit_test").sheet1

    # Читаем все строки
    rows = sheet.get_all_values()


    spreadsheet=client.open_by_key("1SAWJrKfZEcGM1HGBWfIHg5pdEh9aaQfyjmGjXwKIn8U")
    sheet = spreadsheet.worksheet('Транзит')

    print(sheet.acell('E9').address)

    print(f"Searching {model}...")
    model_list = list()
    for i, row in enumerate(rows, start=1):
        if model.lower() in row[1].lower() and row[0] != "":
            link = "https://docs.google.com/spreadsheets/d/1SAWJrKfZEcGM1HGBWfIHg5pdEh9aaQfyjmGjXwKIn8U/edit?"\
                   "gid=1068582570#gid=1068582570&range=B{}".format(i)
            row.insert(0, link)
            model_list.append(row)

    return model_list

