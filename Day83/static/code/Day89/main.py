from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CONFIGURE TABLE
class Todo(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    task: Mapped[str] = mapped_column(String(250), nullable=False)
    has_done: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

class TodoForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    has_done = BooleanField('has_done', validators=[DataRequired()])
    submit = SubmitField('Submit')

with app.app_context():
    db.create_all()

# @app.route('/')
@app.route('/', methods=['GET', 'POST'])
def get_all_todos():
    # Query the database for all the todos. Convert the data to a python list.
    result = db.session.execute(db.select(Todo))
    all_todos = result.scalars().all()
    # print(all_todos)
    # todos = all_todos

    # todos_do = db.session.execute(db.select(Todo).where(Todo.has_done == 0)).scalars()
    # todos_done = db.session.execute(db.select(Todo).where(Todo.has_done == 1)).scalars()
    todos_do = db.session.query(Todo).filter_by(has_done=False).order_by(Todo.id.desc()).all()
    todos_done = db.session.query(Todo).filter_by(has_done=True).order_by(Todo.id.desc()).all()
    # print(todos_do)
    # print(todos_done)

    add_form = TodoForm()
    if request.method == 'POST':
        print(f"text = {add_form.task.data}")
        new_task           = add_form.task.data
        # new_has_done       = add_form.has_done.data
        new_has_done       = False
        new_todo = Todo(
            task           = new_task,
            has_done       = new_has_done,
        )

        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('get_all_todos'))
    return render_template("index.html", todos_do=todos_do, todos_done=todos_done, form=add_form)


# done_todo() to change an existing blog todo
@app.route('/done-todo/<int:todo_id>', methods=["GET", "POST"])
def done_todo(todo_id):
    todo_has_done = db.get_or_404(Todo, todo_id)

    todo_has_done.has_done = True
    db.session.commit()
    return redirect(url_for('get_all_todos'))


# edit_todo() to change an existing blog todo
@app.route('/edit-todo/<int:todo_id>', methods=["GET", "POST"])
def edit_todo(todo_id):
    todo_to_update = db.get_or_404(Todo, todo_id)

    edit_form = TodoForm(
        task=todo_to_update.task,
        has_done=todo_to_update.has_done,
    )
    if request.method == 'POST':
        new_task     = edit_form.task.data
        new_has_done = edit_form.has_done.data
        todo_to_update.task     = new_task
        todo_to_update.has_done = new_has_done
        db.session.commit()
        return redirect(url_for('get_all_todos'))
    else:
        return render_template("make-todo.html", form=edit_form, post_h1="Edit Todo")

# delete_todo() to remove a blog todo from the database
@app.route('/delete/<int:todo_id>', methods=["GET", "POST"])
def delete_todo(todo_id):
    todo_to_delete = db.get_or_404(Todo, todo_id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_todos'))



if __name__ == "__main__":
    app.run(debug=True, port=5003)
