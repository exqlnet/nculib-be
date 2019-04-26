from flask import Blueprint

book_blueprint = Blueprint("book", __name__)

from flask_restful import Api
from .resource.query import BookQuery

book_api = Api(book_blueprint)

book_api.add_resource(BookQuery, "/query")
