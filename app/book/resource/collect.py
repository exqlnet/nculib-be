from flask_restful import Resource
from app import db
from flask import g
from app.book.model.book import Book
from app.utils.decorators import login_required
from app.utils.parser import add_args


class UserCollect(Resource):
    method_decorators = [login_required]

    def get(self):
        """获取用户收藏的所有书籍"""
        return {
            "status": 1,
            "message": "获取成功",
            "data": [book.to_json_brief() for book in g.current_user.collect_books]
        }

    def post(self):
        """收藏一本书"""
        args = add_args([
            ["bookId", int, True, 0, "哪本书？"]
        ]).parse_args()
        book = Book.query.get(args["bookId"])
        if not book:
            return {
                "status": 0,
                "message": "收藏失败！找不到该书！"
            }
        g.current_user.collect_books.append(book)
        db.session.commit()
        return {
            "status": 1,
            "message": "收藏成功"
        }

    def delete(self):
        """取消收藏一本书"""
        args = add_args([["bookId", int, True, 0, "哪本书？"]]).parse_args()
        book = Book.query.get(args["bookId"])
        if not book:
            return {
                "status": 0,
                "message": "取消收藏失败！找不到该书！"
            }
        g.current_user.collect_books.remove(book)
        db.session.commit()
        return {
            "status": 1,
            "message": "取消收藏成功"
        }
