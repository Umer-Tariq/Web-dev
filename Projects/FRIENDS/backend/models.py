from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Friend(db.Model):
    __tablename__ = 'Friend'

    fid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    role = db.Column(db.String(50), nullable = False)
    description = db.Column(db.Text, nullable = False)
    gender = db.Column(db.String(10), nullable = False)
    img_url = db.Column(db.String(200), nullable = False)

    def __repr__(self):
        return f'{self.name}'
    
    def to_json(self):
        response = {
            'id' : self.fid,
            'name' : self.name,
            'role' : self.role,
            'description' : self.description,
            'gender' : self.gender,
            'imgUrl' : self.img_url
        }

        return response