import pickle
from typing import Any
import imgsearch
from datetime import datetime

from config import FIELDS, TABLE_LINK


def parse_date(x):
    try:
        date = x[FIELDS["ARRIVAL_DATE"]]
        if date:
            return datetime.strptime(date, "%d.%m.%Y")
        return datetime.max
    except ValueError:
        return datetime.max


def search_cars(request: str = None) -> list[Any]:

    with open("data.pkl", "rb") as f:
        rows = pickle.load(f)

    print(f"Searching {request}...")
    model_list = []

    imgdict = imgsearch.get_img_dict()

    for i, row in enumerate(rows, start=1):

        if (
            request.lower() in row[FIELDS["NOMENCLATURE_NAME"]].lower()
            and row[FIELDS["VIN"]] != ""
        ):

            link = TABLE_LINK.format(i)
            row_copy = row.copy()

            row_copy.insert(0, link)

            if i in imgdict:
                row_copy.insert(0, imgdict[i])
            else:
                row_copy.insert(0, "")

            row_copy.append(i)
            model_list.append(row_copy)

    # сортировка по дате
    model_list.sort(key=parse_date)

    # сначала "в наличии"
    model_list.sort(
        key=lambda x: not (
            "в наявност" in x[FIELDS["STATUS"]].lower()
            or "в наявност" in x[FIELDS["STORAGE"]].lower()
        )
    )

    # потом по резерву
    model_list.sort(key=lambda x: bool(x[FIELDS["RESERVE"]]))

    for row in model_list:
        if not row[FIELDS["STATUS"]]:
            row[FIELDS["STATUS"]] = "-"
        if not row[FIELDS["STORAGE"]]:
            row[FIELDS["STORAGE"]] = "-"
        if not row[FIELDS["RESERVE"]]:
            row[FIELDS["RESERVE"]] = "-"

    return model_list


if __name__ == "__main__":
    for i in search_cars("Avatr 07"):
        print(i[FIELDS["STORAGE"]])