from app import db


class Book(db.Model):
    """图书信息"""
    __tablename__ = "books"

    book_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, index=True)
    press_time = db.Column(db.Date())
    isbn = db.Column(db.String(128))
    price = db.Column(db.DECIMAL(5, 2))
    category = db.Column(db.String(128))
    coden = db.column(db.String(128))  # 分类号
    total_page = db.Column(db.Integer)
    summary = db.column(db.Text)

    press_id = db.Column(db.Integer, db.ForeignKey("press.press_id"))
    author_id = db.Column(db.Integer, db.ForeignKey("authors.author_id"))


class Author(db.Model):
    """作者"""
    __tablename__ = "authors"

    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))


class Press(db.Model):
    """出版社"""
    __tablename__ = "press"

    press_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
