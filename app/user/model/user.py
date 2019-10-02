from app import db
from datetime import datetime
from flask import current_app
from werkzeug.security import check_password_hash, generate_password_hash
from itsdangerous import JSONWebSignatureSerializer, BadSignature

user_collect = db.Table("user_collect",
                        db.Column("user_id", db.Integer, db.ForeignKey("user.user_id"), primary_key=True),
                        db.Column("book_id", db.Integer, db.ForeignKey("books.book_id"), primary_key=True))


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    open_id = db.Column(db.String(256), unique=True)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    lib_paswd_hash = db.Column(db.String(128), default=None)

    collect_books = db.relationship("Book", secondary=user_collect, backref='user')
    search_history = db.relationship("Book")

    def get_id(self):
        return str(self.user_id)  # 最好是学号

    def verify_passwd(self, passwd):
        return check_password_hash(self.lib_paswd_hash, passwd)

    def set_passwd(self, old_passwd, new_passwd):
        """如果未储存过密码，则传入old_passwd为None，初始化密码为new_passwd，否则需要传入old_passwd进行更改密码"""
        if not old_passwd:
            if not self.lib_paswd_hash:
                self.lib_paswd_hash = generate_password_hash(new_passwd)
            else:
                return ValueError  # 如果旧密码已存在，则要求输入旧密码，否则返回Error
        else:
            try:
                if check_password_hash(self.lib_paswd_hash, old_passwd):
                    self.lib_paswd_hash = generate_password_hash(new_passwd)
                else:
                    return PermissionError
            except:
                return PermissionError

    def generate_token(self, paswd):
        s = JSONWebSignatureSerializer(current_app.config['SECRET_KEY'])
        s.dumps({'id': self.user_id, 'paswd': paswd})

    def verify_token(self, token):
        s = JSONWebSignatureSerializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except BadSignature:
            return None
        if data.get['id']:
            if data.get['xh'] and data.get['xh'] == self.user_id:
                ...
            if data.get['id'] != self.user_id:
                return 0  # 若解析出别人的token则返回0
        else:
            return True
