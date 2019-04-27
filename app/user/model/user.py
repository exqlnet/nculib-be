from app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    open_id = db.Column(db.String(256), unique=True)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    setting = db.Column(db.String(256), default="[]")
