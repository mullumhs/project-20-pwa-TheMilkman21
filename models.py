from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)

    director = db.Column(db.String(100), nullable=False)

    release_date = db.Column(db.Integer, nullable=False)

    
    
    

