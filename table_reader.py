import pickle
from typing import Any
import imgsearch
from datetime import datetime

def parse_date(x):
    try:
        if x[18]:
            return datetime.strptime(x[18], "%d.%m.%Y")
        else:
            return datetime.max  # пустые даты будут в конце
    except ValueError:
        return datetime.max  # некорректные или пустые даты в конец

def search(request: str = None) -> list[Any]:

    rows = None

    with open("data.pkl", "rb") as f:
        rows = pickle.load(f)


    print(f"Searching {request}...")
    model_list = list()
    # retrieving appropriate rows
    for i, row in enumerate(rows, start=1):
        print(row[23])
        if request.lower() in row[23].lower() and row[0] != "":
            link = "https://docs.google.com/spreadsheets/d/1PNjWz8LTArpcRovsEUTjd543oEjRHeh7D_N8o4EhIvA/edit?"\
                   "gid=1640256538#gid=1640256538&range=B{}".format(i)
            row.insert(0, link)

            imgdict = imgsearch.get_img_dict()
            if i in imgdict:
                row.insert(0, imgdict[i])
            else:
                row.insert(0, "")


            model_list.append(row)

    # sorting list

    model_list.sort(key=parse_date)

    model_list = ([i for i in model_list if "в наявност" in i[20].lower() or "в наявност" in i[21].lower()]
                  + [i for i in model_list if "в наявност" not in i[20].lower() or "в наявност" not in i[21].lower()])

    model_list = [i for i in model_list if not i[22]] + [i for i in model_list if i[22]]

    for i in model_list:
        if not i[22]:
            i[22] = "-"
        if not i[18]:
            i[18] = "-"


    return model_list

if __name__ == "__main__":
    for i in search("Avatr 07"):
        print(i[21])
