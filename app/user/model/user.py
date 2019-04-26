from app import db


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    access_key = db.Column(db.String(256), unique=True)
