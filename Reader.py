import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pickle
from time import sleep
import threading
import logging

from config import SCOPE, SHEET, SHEET_COPY, DATA, CREDS

logger = logging.getLogger(__name__)

class Reader(threading.Thread):
    def __init__(self):
        super().__init__()

    def read_table(self):

        creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS, SCOPE)
        client = gspread.authorize(creds)

        sheet = client.open(SHEET).sheet1

        rows = sheet.get_all_values()
        logging.info("Scanned table")
        with open(DATA, "wb") as f:
            pickle.dump(rows, f)


    def run(self):
        while True:

            self.read_table()
            sleep(15)


if __name__ == "__main__":
    r = Reader()
    r.run()