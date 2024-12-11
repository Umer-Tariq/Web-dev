from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    name = db.Column(db.Text)
    uid = db.Column(db.Integer, primary_key = True)
    age = db.Column(db.Integer, nullable = True)

    def __repr__(self):
        return f'{self.name}, {self.age}'