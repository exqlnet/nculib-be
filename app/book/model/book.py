from app import db
from jieba.analyse.analyzer import ChineseAnalyzer


class Book(db.Model):
    """图书信息"""
    __tablename__ = "books"
    __searchable__ = ["name", "isbn", "classification", "summary"]
    __analyzer__ = ChineseAnalyzer()

    book_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, index=True)
    press_time = db.Column(db.String(128))
    isbn = db.Column(db.String(128))
    price = db.Column(db.DECIMAL(8, 2))
    classification = db.Column(db.String(128))  # 分类号
    total_page = db.Column(db.Integer)
    summary = db.Column(db.Text)
    lib_id = db.Column(db.String(128))  # 对应图书馆url里的id

    press = db.relationship("Press")
    author = db.relationship("Author")
    category = db.relationship("Category")

    press_id = db.Column(db.Integer, db.ForeignKey("press.press_id"))
    author_id = db.Column(db.Integer, db.ForeignKey("authors.author_id"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.category_id"))

    def to_json(self):
        return {
            "bookId": self.book_id,
            "bookName": self.name,
            "pressTime": self.press_time,
            "isbn": self.isbn,
            "price": self.price,
            "classification": self.classification,
            "totalPage": self.total_page,
            "summary": self.summary
        }


class Author(db.Model):
    """作者"""
    __tablename__ = "authors"

    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)


class Press(db.Model):
    """出版社"""
    __tablename__ = "press"

    press_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)


class Category(db.Model):
    """学科分类"""
    __tablename__ = "category"

    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)


class BookRecommendCategory(db.Model):
    """书籍推荐目录设置"""
    __tablename__ = "book_recommend_category"

    rc_id = db.Column(db.Integer)
    name = db.Column(db.String(128))


user_category_setting = db.Table(
    db.Column("user_id", db.Integer, db.ForeignKey("user.user_id"), primary_key=True),
    db.Column("rc_id", db.Integer, db.ForeignKey("book_recommend_category.rc_id"), primary_key=True)
)

