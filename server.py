from flask import Flask, request, render_template
import table_reader as tr
from Reader import Reader
import threading

readert = Reader()
t = threading.Thread(target=readert.run, daemon=True)
t.start()


app = Flask(__name__)

@app.route("/", methods=["GET"])
def search_page():
    query = request.args.get("q", "")
    results = None
    if query:
        results = tr.search(query)
    return render_template("index.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
