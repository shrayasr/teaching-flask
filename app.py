from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

list_of_customers = [
        "Bharati Bhawan",
        "Ramakrishna Mutt"
        ]

@app.route("/")
def index():
    return render_template("index.html", now=str(datetime.now()))

@app.route("/customers/", methods=["GET","POST"])
def customers():
    if request.method == "GET":
        return render_template("customers.html", customers=list_of_customers)
    elif request.method == "POST":
        try:
            customer_name = request.form["customer-name"].strip()
            if len(customer_name) > 0:
                list_of_customers.append(customer_name)
            return redirect(url_for("customers"))
        except Exception as e:
            print e
            return redirect(url_for("customers"))

if __name__ == "__main__":
    app.run(debug=True)
