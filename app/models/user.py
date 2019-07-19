import uuid
from app.db import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(db.Model):
    __tablename__ = 'user'
    userid = db.Column(db.String, primary_key=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, userid, first_name, last_name, email, password):
        self.userid = userid
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def json(self):
        return {
            'userid': self.userid,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email  
        }

    def set_password(self):
        self.password = generate_password_hash(self.password)

    def check_password(self, passwd_hash):
        return check_password_hash(self.password, passwd_hash)

    @classmethod
    def find_by_email(cls, email):
        print('find, by:', email)
        return cls.query.filter_by(email=email).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()

