import pickle

def search(request:str = None):

    rows = None

    with open("data.pkl", "rb") as f:
        rows = pickle.load(f)


    print(f"Searching {request}...")
    model_list = list()
    for i, row in enumerate(rows, start=1):
        if request.lower() in row[22].lower() and row[0] != "" and not row[19]:
            link = "https://docs.google.com/spreadsheets/d/1PNjWz8LTArpcRovsEUTjd543oEjRHeh7D_N8o4EhIvA/edit?"\
                   "gid=1640256538#gid=1640256538&range=B{}".format(i)
            row.insert(0, link)
            model_list.append(row)

    return model_list


