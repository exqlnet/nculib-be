from app import db
from datetime import datetime

user_collect = db.Table("user_collect",
                        db.Column("user_id", db.Integer, db.ForeignKey("user.user_id"), primary_key=True),
                        db.Column("book_id", db.Integer, db.ForeignKey("books.book_id"), primary_key=True))


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    open_id = db.Column(db.String(256), unique=True)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    preference = db.Column(db.String(256), default="[]")

    collect_books = db.relationship("Book", secondary=user_collect)
