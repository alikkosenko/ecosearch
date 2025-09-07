import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pickle
from time import sleep
import threading

from config import SCOPE, SHEET, DATA, CREDS

class Reader(threading.Thread):
    def __init__(self):
        super().__init__()

    def read_table(self):

        creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS, SCOPE)
        client = gspread.authorize(creds)

        sheet = client.open(SHEET).sheet1

        rows = sheet.get_all_values()

        with open(DATA, "wb") as f:
            pickle.dump(rows, f)


    def run(self):
        while True:

            self.read_table()
            sleep(30)


if __name__ == "__main__":
    r = Reader()
    r.run()