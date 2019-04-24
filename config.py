
class Default:
    
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost/nculib?charset=utf8"


class Development(Default):

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@fucheng360.top/nculib?charset=utf8"


config = {
    "default": Default,
    "dev": Development
}
