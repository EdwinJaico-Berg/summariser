from flask import Flask, render_template, request
from summariser import summarise_webpage

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        
        url = request.form.get("url")

        bullet_points = summarise_webpage(url)

        return render_template("index.html", bullet_points=bullet_points)
    
    else:

        bullet_points = None

        return render_template("index.html", bullet_points=bullet_points)

@app.route("/text")
def text():
    return render_template("text.html")


if __name__ == '__main__':
    app.run()