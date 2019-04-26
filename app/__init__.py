from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
import flask_whooshalchemyplus

db = SQLAlchemy()


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name))
    # 全文索引
    flask_whooshalchemyplus.init_app(app)

    db.init_app(app)

    from app.book import book_blueprint
    app.register_blueprint(book_blueprint, url_prefix="/api/book")

    app.app_context().push()
    db.create_all()
    return app
