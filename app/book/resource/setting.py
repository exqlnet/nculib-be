from flask_restful import Resource
from app.book.model.book import Subject, Category, db
from app.utils.parser import add_args
from app.utils.decorators import login_required
import json
from flask import g


class SubjectSetting(Resource):

    def get(self):
        """获取所有学科选项"""
        subjects = Subject.query.all()
        return {
            "status": 1,
            "message": "获取成功",
            "data": [subject.to_json() for subject in subjects]
        }


class UserSubjectSetting(Resource):
    method_decorators = login_required

    def get(self):
        """获取推送设置"""
        return {
            "status": 1,
            "message": "获取成功",
            "data": json.loads(g.current_user.setting)
        }

    def put(self):
        """修改推送设置"""
        args = add_args([
            ["subjects", list, True, [], "哪些category？"]
        ])
        subject_ids = list(filter(lambda x: type(x) == int, args["categories"]))
        subjects = Subject.query.filter(Subject.subject_id.in_(subject_ids))
        if len(subjects) != len(subject_ids):
            return {
                "status": 0,
                "message": "提交有误",
            }
        g.current_user.setting = json.dumps(subject_ids)
        db.session.commit()
        return {
            "status": 1,
            "message": "设置成功"
        }
