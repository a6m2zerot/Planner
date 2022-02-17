from app import app
from flask import render_template, request


@app.route('/', methods=["GET", "POST"])
def index():  # project view
    projects = [1]
    if request.method == "POST":
        projects.append(0)
    return render_template("index.html", projects=projects)


@app.route('/calendar')
def calendar():  # calendar view
    return render_template("calendar.html")
