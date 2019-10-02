import os


class Default:
    
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost/nculib?charset=utf8"
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
                 '8e127c14-9ae0-4726-9a0d-137f64de3e47'


class Development(Default):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@fucheng360.top/nculib?charset=utf8"


config = {
    "default": Default,
    "dev": Development
}
