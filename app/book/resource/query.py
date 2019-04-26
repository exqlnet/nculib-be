from flask_restful import Resource
from app.utils.parser import add_args
from app.book.model.book import Book


class BookQuery(Resource):

    def get(self):
        """查询图书"""
        args = add_args([
            ["fulltext", bool, False, False, "是否全文索引？"],
            ["key", str, True, None, "关键词？"],
            ["per_page", int, False, 20, "每页显示多少？"],
            ["page", int, False, 1, "第几页？？"]
        ], "args").parse_args()

        if not args.get("fulltext", False):
            """根据题名查找"""
            pagination = Book.query.filter(Book.name.like("%{}%".format(args.get("key"))))\
                .paginate(per_page=args.get("per_page"),
                          page=args.get("page"), error_out=True)

            return {
                "status": 0,
                "message": "获取成功",
                "data": [book.to_json() for book in pagination.items],
                "total_page": pagination.total,
                "page": pagination.page
            }
        else:
            # todo 全文索引查找
            books = []
            for i, book in Book.query:
                if i > 20:
                    break
                books.append(book.to_json())
            return {
                "status": 0,
                "message": "获取成功",
                "data": books,
            }
