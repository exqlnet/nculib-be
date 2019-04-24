# from app.book.model.book import *
from app import create_app
from app.book.model.book import *
from pymongo import MongoClient
import re
mongo = MongoClient("mongodb://localhost:27017")

create_app("dev").app_context().push()

datas = mongo.lib.datas

result = datas.find({})


def parse_one(dic):
    res = {
        "isbn": "不明",
        "name": "不明",
        "press_time": "不明",
        "category": "不明",
        "classify": "不明",
        "total_page": 0,
        "summary": "不明",
        "price": 0,
        "author": "不明",
        "press": "不明",
        "discard": False,
        "coden": "不明"
    }

    if dic.get("ISBN及定价:"):
        """isbn和定价"""
        s = dic.get("ISBN及定价:").split("/")
        # print(s)
        if len(s) == 1:
            res["isbn"] = s[0].split(" ")[0]
        else:
            res["isbn"] = s[0].split(" ")[0]

            _reg = re.findall(r"\d+\.{0,1}\d+", s[1])
            res["price"] = float(_reg[0]) if _reg else "不明"

        if not is_isbn(res["isbn"]):
            res["isbn"] = "不明"

    if dic.get("题名/责任者:"):
        """书名"""
        name = get_a_text(dic.get("题名/责任者:"))
        res["name"] = name
        # print(name, dic.get("题名/责任者:"))
    else:
        res["discard"] = True

    if dic.get("个人责任者:"):
        """作者"""
        author = get_a_text(dic.get("个人责任者:"))
        res["author"] = author
        # print(author)

    if dic.get("出版发行项:"):
        """出版社和出版年份"""
        try:
            s = dic.get("出版发行项:").split(",")
            press_time = s[1]
            press = s[0].split(":")[1]
            # print(press_time, press)
            res["press_time"] = press_time
            res["press"] = press
        except Exception:
            # print(dic.get("出版发行项:"))
            res["discard"] = True

    if dic.get("中图法分类号:"):
        res["classify"] = get_a_text(dic.get("中图法分类号:"))
        # print(res["classify"])

    if dic.get("载体形态项:"):
        """页数"""
        try:
            res["total_page"] = re.findall(r"(\d+?)页", dic.get("载体形态项:"))[0]
        except Exception:
            res["discard"] = True

    if dic.get("学科主题:"):
        """学科分类"""
        res["category"] = get_a_text(dic.get("学科主题:"))
        # print(res["category"])

    if dic.get("提要文摘附注:"):
        """摘要summary"""
        res["summary"] = dic.get("提要文摘附注:")

    # if dic.get("isbn") == " ":
    # print(dic.get("ISBN及定价:"))
    return res


def is_isbn(string):
    if not re.findall("[0-9]+-[0-9]+-[0-9]+[0-9]+", string):
        return False
    return True


def get_a_text(string):
    reg = re.findall("<.+?>(.+?)<.+?>", string)
    return reg[0] if reg else "不明"


# """配置数据库"""
# import pymysql
#
# db_config = {
#     "host": "fucheng360.top",
#     "user": "root",
#     "passwd": "123456",
#     "port": 3306,
#     "database": "nculib",
#     "charset": "utf8",
# }
# conn = pymysql.connect(**db_config)
# cu = conn.cursor()

authors = set()
categories = set()
presses = set()
for a in Author.query.all():
    authors.add(a.name)
for c in Category.query.all():
    categories.add(c.name)
for p in Press.query.all():
    presses.add(p.name)


discards = []
from tqdm import tqdm
for i, data in tqdm(enumerate(result)):
    if i > 100:
        break
    # parse_one(data)
    res = parse_one(data)

    if res["discard"]:
        discards.append(res)
    """开始导入"""
    if res["category"] in categories:
        category = Category.query.filter_by(name=res["category"]).first()
    else:
        category = Category(name=res["category"])
        db.session.add(category)

    if res["press"] in presses:
        press = Press.query.filter_by(name=res["press"]).first()
        db.session.add(press)
    else:
        press = Press(name=res["press"])

    if res["author"] in authors:
        author = Author.query.filter_by(name=res["author"]).first()
        db.session.add(author)
    else:
        author = Author(name=res["author"])

    book = Book(name=res["name"], press_time=res["press_time"], isbn=res["isbn"],
                price=res["price"], classify=res["classify"], total_page=res["total_page"], summary=res["summary"],
                category=category, author=author, press=press)
    db.session.add(book)
    # cu.execute("insert into ")
    # print(res)
    # print(res["isbn"], is_isbn(res["isbn"]))
    # print(res)

db.session.commit()

with open("discards.txt", "w") as file:
    import json
    file.write(json.dumps(discards, ensure_ascii=False))
