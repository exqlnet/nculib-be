from flask import request, abort, g
from functools import wraps
from flask import g


def login_required(func):

    def wrapper(*args, **kwargs):
        if not g.current_user:
            abort(403)
        return func(*args, **kwargs)

    return wrapper
