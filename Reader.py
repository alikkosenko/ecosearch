import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pickle
from time import sleep
import logging
import threading
import pandas as pd
import os

class Reader(threading.Thread):
    def __init__(self, credentials:str="credenstials.json", sheet:str="Транзит Авто**"):
        super().__init__()
        self.credentials = credentials
        self.sheet = sheet

    def read_table(self):
        scope = ["https://spreadsheets.google.com/feeds",
                 "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        client = gspread.authorize(creds)

        sheet = client.open("Транзит Авто**").sheet1

        rows = sheet.get_all_values()

        with open("data.pkl", "wb") as f:
            pickle.dump(rows, f)


    def run(self):
        while True:
            print("Update")
            self.read_table()
            sleep(30)


if __name__ == "__main__":
    r = Reader()
    r.run()