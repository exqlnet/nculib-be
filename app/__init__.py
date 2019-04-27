from flask import Flask, g, request
from config import config
from flask_sqlalchemy import SQLAlchemy
import flask_whooshalchemyplus

db = SQLAlchemy()


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name))
    db.init_app(app)

    # 全文索引
    flask_whooshalchemyplus.init_app(app)

    from app.book import book_blueprint
    app.register_blueprint(book_blueprint, url_prefix="/api/book")

    app.app_context().push()
    db.create_all()
    # flask_whooshalchemyplus.index_all(app)

    @app.before_request
    def before():
        from app.user.model.user import User
        open_id = request.headers.get("wx_open_id")
        user = User.query.filter_by(open_id=open_id).first()
        if (not user) & (type(open_id) == str):
            if  len(open_id) > 6:
                user = User(open_id=open_id)
                db.session.add(user)
                db.session.commit()
        g.current_user = user

    @app.after_request
    def after(response):
        response.headers["Tech"] = "NCUHOME 2019"
        return response

    return app
