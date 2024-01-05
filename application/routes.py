from flask import render_template, request, flash, redirect
from application import app, db , mongo
from .forms import TodoForm
from datetime import datetime

@app.route("/")
def get_todos():
    todos=[]
    for todo in db.todo.find().sort("date_created", -1):
        todo["_id"]=str(todo["_id"])
        todo["date_created"] = todo["date_created"].strftime("%b %d %Y %H:%M:%S")
        todos.append(todo)
    return render_template("view_todos.html",todos=todos)

@app.route("/add_todo", methods=['POST', 'GET'])
def add_todo():
    if request.method == "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        completed = form.completed.data

        # Access the collection through the PyMongo instance
        mongo.db.todo.insert_one({
            "name": todo_name,
            "description": todo_description,
            "completed": completed,
            "date_created": datetime.utcnow()
        })

        flash("Todo successfully added", "success")
        return redirect("/")
    else:
        form = TodoForm()
    return render_template("add_todo.html", form=form)
