from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300), nullable=False)
    completed=db.Column(db.Boolean(),default=False)

    def __rep__(self):
        return '<Task %r>' % self.id
    