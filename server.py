from flask import Flask, request, render_template, jsonify
import table_reader as tr
from Reader import Reader
import threading
import gspread
import logging

from config import RESERVE, SHEET, SHEET_COPY, STATUS

logging.basicConfig(
    filename="eco.log",
    filemode="a",  # "w" = overwrite, "a" = append
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


readert = Reader()
t = threading.Thread(target=readert.run, daemon=True)
t.start()


app = Flask(__name__)

@app.route("/", methods=["GET"])
def search_page():
    query = request.args.get("q", "")
    results = None
    if query:
        results = tr.search_cars(query)

    logging.info(query)
    return render_template("index.html", query=query, results=results)

@app.route("/vin", methods=["GET"])
def search_vin():
    query = request.args.get("q", "")
    results = None
    if query:
        results = tr.search_cars(query)
    return render_template("vin.html", query=query, results=results)

@app.route("/update_reserve", methods=["POST"])
def update_reserve():
    try:
        data = request.get_json()
        row = data.get("row")   # номер строки приходит из item
        value = data.get("value")

        if row is None or value is None:
            return jsonify({"success": False, "error": "Некорректные данные"})

        # Авторизация gspread
        gc = gspread.service_account(filename="credentials.json")
        sh = gc.open(SHEET).worksheet("Транзит")

        logging.info(data)
        # Преобразуем row в int и value в строку
        sh.update_cell(int(row), RESERVE-1, value)

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route("/update_status", methods=["POST"])
def update_status():
    data = request.get_json()
    row = int(data["row"])
    value = data["value"]

    # Авторизация gspread
    gc = gspread.service_account(filename="credentials.json")
    sheet = gc.open(SHEET).worksheet("Транзит")

    # Здесь RESERVE заменяешь на STATUS
    sheet.update_cell(row, STATUS-1, value)

    return jsonify(success=True, row=row, value=value)



if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
