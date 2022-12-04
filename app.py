from flask import Flask, render_template, request
from summariser import summarise_webpage, summarise_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        
        url = request.form.get("url")

        summary = summarise_webpage(url)

        return render_template("index.html", summary=summary)
    
    return render_template("index.html", summary=None)

@app.route("/text", methods=["GET", "POST"])
def text():
    if request.method == "POST":

        text = request.form.get("text")

        summary = summarise_text(text)

        return render_template("text.html", summary=summary)

    return render_template("text.html", summary=None)


if __name__ == '__main__':
    app.run()