from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", now=str(datetime.now()))

if __name__ == "__main__":
    app.run(debug=True)
