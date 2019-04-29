from app.book.model.book import Subject, Book, Category
import json
from flask_restful import Resource
from app import db
from app.utils.dbtool import to_dic
from app.utils.decorators import login_required
from flask import g
from sqlalchemy import or_
from sqlalchemy.sql.expression import func


def get_recommend_books(subjects):
    sql = """
    select book_id, books.name, press_time, isbn, price, classification, total_page, summary, c.name, a.name, p.name, 'https://img3.doubanio.com/view/subject/l/public/s32266692.jpg' from books
    left join category c on books.category_id = c.category_id
    left join authors a on books.author_id = a.author_id
    left join press p on books.press_id = p.press_id
    {}
    order by rand()
    limit 20
    """
    subject_names = []
    for subject in subjects:
        subject_names.extend(subject.name.split("、"))
    where = "where " + " or ".join(["c.name like '%{}%'".format(name) for name in subject_names])
    if not subjects:
        return []
    sql = sql.format(where)
    return to_dic(sql, None, ["bookId", "bookName", "pressTime", "isbn", "price", "classification", "totalPage", "summary", "category", "author", "press", "cover"])


class Recommend(Resource):

    @login_required
    def get(self):
        pref_subjects = Subject.query.filter(Subject.subject_id.in_(json.loads(g.current_user.preference))).all()
        if not pref_subjects:
            books = [book.to_json() for book in Book.query.order_by(func.rand()).limit(20).all()]
        else:
            # filters = or_(*[Category.name.like("%" + subject.name + "%") for subject in pref_subjects])
            # books = Book.query.filter(filters).order_by(func.rand()).limit(20).all()
            books = get_recommend_books(pref_subjects)

        return {
            "status": 1,
            "message": "获取成功",
            "data": books
        }
