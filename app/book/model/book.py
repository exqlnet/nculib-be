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

    def to_json_brief(self):
        return {
            "bookId": self.book_id,
            "bookName": self.name,
            "summary": self.summary,
            "cover": "https://img3.doubanio.com/view/subject/l/public/s32266692.jpg",
            "author": self.author.name
        }

    def to_json_detail(self):
        return {
            "bookId": self.book_id,
            "bookName": self.name,
            "pressTime": self.press_time,
            "isbn": self.isbn,
            "price": float(self.price),
            "classification": self.classification,
            "totalPage": self.total_page,
            "summary": self.summary,
            "author": self.author.name,
            "press": self.press.name,
            "category": self.category.name,
            "cover": "https://img3.doubanio.com/view/subject/l/public/s32266692.jpg"
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


class Subject(db.Model):
    """书籍推荐的学科设置"""
    __tablename__ = "book_recommend_category"

    subject_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)

    def to_json(self):
        return {
            "subjectId": self.subject_id,
            "subjectName": self.name
        }

    def to_json_user(self, ids):
        return {
            "subjectId": self.subject_id,
            "subjectName": self.name,
            "checked": self.subject_id in ids
        }
