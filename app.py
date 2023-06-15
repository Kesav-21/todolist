from flask import Flask,render_template,request,redirect
from database import db,Todo

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db.init_app(app)

@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error while adding the task'

    else:
        tasks = Todo.query.all()
        return render_template("index.html", tasks=tasks)
    
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/listtask')
    except:
        return 'There was an error while deleting that task'
    
@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/listtask')
        except:
            return 'There was an issue while updating that task'

    else:
        return render_template('update.html', task=task)
    
@app.route('/mark/<int:id>',methods=['GET','POST'])
def mark(id):
    task_to_mark_completed=Todo.query.get_or_404(id)
    task_to_mark_completed.completed = True
    db.session.commit()

    # Redirect to the main page or any other appropriate page
    return redirect('/listtask')

@app.route('/listtask')
def listtask():
    tasks = Todo.query.all()
    return render_template("listtask.html", tasks=tasks)

@app.route('/addtask',methods=['POST','GET'])
def addtask():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/addtask')
        except:
            return 'There was an error while adding the task'
    else:
        return render_template('addtask.html')

if __name__=="__main__":
    app.run(debug=True)