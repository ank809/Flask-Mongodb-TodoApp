from flask import render_template
from application import app
from .forms import Todo_Form
@app.route("/")

def index():
    return render_template("view_todos.html", title="Layout Page")

@app.route("/add_todo")
def add_todo():
    form =Todo_Form()
    return render_template("add_todo.html", form=form)