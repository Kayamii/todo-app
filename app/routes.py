from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Todo

# Create a Blueprint for the routes
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@main_bp.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    new_todo = Todo(task=task)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/complete/<int:todo_id>')
def complete(todo_id):
    todo = Todo.query.get(todo_id)
    todo.completed = True
    db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/test')
def test():
    return "Flask is working!"
