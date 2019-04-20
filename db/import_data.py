# from app.book.model.book import *
# from app import create_app
from pymongo import MongoClient
from pprint import pprint
import re
db = MongoClient("mongodb://localhost:27017")

# create_app().app_context().push()

datas = db.lib.datas

result = datas.find({})


def parse_one(dic):
    res = {
        "isbn": "不明",
        "name": "不明",
        "press_time": "不明",
        "category": "不明",
        "coden": "不明",
        "total_page": "不明",
        "summary": "不明",
        "price": "不明",
        "author": "不明",
        "press": "不明",
        "classify": "不明",
        "discard": False
    }

    if dic.get("ISBN及定价:"):
        """isbn和定价"""
        s = dic.get("ISBN及定价:").split("/")
        # print(s)
        if len(s) == 1:
            res["isbn"] = s[0].split(" ")[0]
        else:
            res["isbn"] = s[0].split(" ")[0]
            res["price"] = float(re.findall("[0-9]+.[0-9]+", s[1])[0])

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
            res["total_page"] = re.findall("(.+?)页", dic.get("载体形态项:"))[0]
        except Exception:
            res["discard"] = True

    if dic.get("学科主题:"):
        """学科分类"""
        res["category"] = get_a_text(dic.get("学科主题:"))
        # print(res["category"])


    # if dic.get("isbn") == " ":
    # print(dic.get("ISBN及定价:"))
    return res


def is_isbn(string):
    if not re.findall("[0-9]+-[0-9]+-[0-9]+[0-9]+", string):
        return False
    return True


def get_a_text(string):
    return re.findall("<.+?>(.+?)<.+?>", string)[0]


for i, data in enumerate(result):
    if i > 100:
        break
    # parse_one(data)
    res = parse_one(data)
    print(res)
    # print(res["isbn"], is_isbn(res["isbn"]))
