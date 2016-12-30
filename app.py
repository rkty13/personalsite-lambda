from flask import Flask
from flask import render_template

app = Flask(__name__)

app.config.from_pyfile("config.py")

@app.route("/")
def index():
    return render_template("index.html", 
            host = app.config["STATIC_HOST"],
            scrobble_key = app.config["SCROBBLE_KEY"])

if __name__ == "__main__":
    app.run(debug = app.config["DEBUG"])