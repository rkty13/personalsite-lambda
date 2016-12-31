from flask import Flask
from flask import render_template
from flask import redirect

app = Flask(__name__)

app.config.from_pyfile("config.py")

@app.route("/")
def index():
    return render_template("index.html", 
            host = app.config["STATIC_HOST"],
            scrobble_key = app.config["SCROBBLE_KEY"])

@app.route("/resume.pdf")
@app.route("/resume")
def resume():
    return redirect("https://s3.amazonaws.com/rkty13-personalsite/resume.pdf")

if __name__ == "__main__":
    app.run(debug = app.config["DEBUG"])