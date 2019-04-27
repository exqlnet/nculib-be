from app.book.model.book import Subject
import json
from flask_restful import Resource
from app import db
from app.utils.dbtool import to_dic
from app.utils.decorators import login_required


def get_recommend_books(subjects):
    sql = """
    select book_id, books.name, press_time, isbn, price, classification, total_page, summary, c.name from books
    left join category c on books.category_id = c.category_id
    
    """
    where = "where " + " or ".join(["c.name like '%{}%'".format(subject.name) for subject in subjects])
    sql += where
    return to_dic(sql, None, ["book_id", "bookName", "press_time", "isbn", "price", "classification", "total_page", "summary", "categoryName"])


class Recommend(Resource):

    @login_required
    def get(self):
        pref_subjects = Subject.query.filter(Subject.subject_id.in_(json.loads(g.current_user.preference)))
        books = get_recommend_books(pref_subjects)

        return {
            "status": 1,
            "message": "获取成功",
            "data": books
        }
