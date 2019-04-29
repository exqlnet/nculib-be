from flask import Blueprint

book_blueprint = Blueprint("book", __name__)

from flask_restful import Api
from .resource.query import BookQuery
from .resource.setting import SubjectSetting, UserSubjectSetting
from .resource.recommend import Recommend

book_api = Api(book_blueprint)

book_api.add_resource(BookQuery, "/query")
book_api.add_resource(SubjectSetting, "/subject/setting")
book_api.add_resource(UserSubjectSetting, "/subject/info")
book_api.add_resource(Recommend, "/recommend")
