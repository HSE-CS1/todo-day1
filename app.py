from flask import Flask, render_template, request, redirect

app = Flask(__name__)

TODOS = ["Feed the dog", "Do homework"]
DATES = ["2025-02-10", "2025-02-11"]

@app.route("/")
def index():
    return render_template("index.html", num_tasks=len(TODOS))

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/success")
def success():
    # get the task from the form
    task = request.args.get("task", "")
    task_date = request.args.get("task-date", "")
    if task == "":
        msg = "No task was entered."
        return render_template("error.html", error_msg=msg)
    elif task_date == "":
        msg = "That date is invalid"
        return render_template("error.html", error_msg=msg)
    else:
        # now add it to the TODOS list
        TODOS.append(task)
        DATES.append(task_date)
        return redirect("/show")

@app.route("/show")
def show():
    num_items = len(TODOS)
    # this will show all the tasks in our TODOS list
    return render_template("show.html", num_items=num_items,
                                todos_list=TODOS, task_dates=DATES)
