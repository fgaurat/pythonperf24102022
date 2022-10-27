from flask import Flask,render_template
from Todo import Todo
from TodoDAO import TodoDAO

app = Flask(__name__)

@app.route("/")
def hello_world():
    dao = TodoDAO('todos_db.sqlite')
    todos = dao.getAll()
    return render_template('todos.html',todos=list(todos))


@app.route("/toto")
def une_fonction():
    return "<h1>hello</h1>"