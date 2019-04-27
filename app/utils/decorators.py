from flask import request, abort
from functools import wraps


def login_required(func):

    def wrapper(*args, **kwargs):
        if not request.headers.get("wx_open_id"):
            abort(403)
        return func(*args, **kwargs)

    return wrapper
