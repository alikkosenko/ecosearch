import pickle
from typing import Any
import imgsearch

def search(request: str = None) -> list[Any]:

    rows = None

    with open("data.pkl", "rb") as f:
        rows = pickle.load(f)


    print(f"Searching {request}...")
    model_list = list()
    # retrieving appropriate rows
    for i, row in enumerate(rows, start=1):
        if request.lower() in row[22].lower() and row[0] != "":
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
    model_list = ([i for i in model_list if "в наявност" in i[19].lower() or "в наявност" in i[20].lower()]
                  + [i for i in model_list if "в наявност" not in i[19].lower() or "в наявност" not in i[20].lower()])
    model_list = [i for i in model_list if not i[21]] + [i for i in model_list if i[21]]



    return model_list

if __name__ == "__main__":
    for i in search("Avatr 07"):
        print(i[21])
