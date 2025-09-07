import pickle
from typing import Any
import imgsearch
from datetime import datetime

# Константы с номерами столбцов
from config import ARRIVAL_DATE, NOMENCLATURE_NAME, IMG_NAME, VIN, STATUS, STORAGE, RESERVE, TABLE_LINK



def parse_date(x):
    try:
        if x[ARRIVAL_DATE]:
            return datetime.strptime(x[ARRIVAL_DATE], "%d.%m.%Y")
        else:
            return datetime.max  # пустые даты будут в конце
    except ValueError:
        return datetime.max  # некорректные или пустые даты в конец


def search_cars(request: str = None) -> list[Any]:

    rows = None
    with open("data.pkl", "rb") as f:
        rows = pickle.load(f)

    print(f"Searching {request}...")
    model_list = list()
    # retrieving appropriate rows
    for i, row in enumerate(rows, start=1):
        if request.lower() in row[NOMENCLATURE_NAME].lower() and row[VIN] != "":
            link = TABLE_LINK.format(i)
            row.insert(0, link)

            imgdict = imgsearch.get_img_dict()
            if i in imgdict:
                row.insert(0, imgdict[i])
            else:
                row.insert(0, "")


            model_list.append(row)

    # sorting list
    model_list.sort(key=parse_date)

    model_list = ([i for i in model_list if "в наявност" in i[STATUS].lower() or "в наявност" in i[STORAGE].lower()]
                  + [i for i in model_list if "в наявност" not in i[STATUS].lower() or "в наявност" not in i[STORAGE].lower()])
    model_list = [i for i in model_list if not i[RESERVE]] + [i for i in model_list if i[RESERVE]]

    for i in model_list:
        if not i[STATUS]:
            i[STATUS] = "-"
        if not i[STORAGE]:
            i[STORAGE] = "-"

    return model_list

if __name__ == "__main__":
    for i in search_cars("Avatr 07"):
        print(i[STORAGE])
