from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

list_of_customers = [
        "Bharati Bhawan",
        "Ramakrishna Mutt"
        ]

@app.route("/")
def index():
    return render_template("index.html", now=str(datetime.now()))

@app.route("/customers/")
def customers():
    return render_template("customers.html", customers=list_of_customers)

if __name__ == "__main__":
    app.run(debug=True)
