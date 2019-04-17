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
        "price": "不明"
    }

    if dic.get("ISBN及定价:"):
        s = dic.get("ISBN及定价:").split("/")
        # print(s)
        if len(s) == 1:
            res["isbn"] = s[0]
        else:
            res["isbn"] = s[0]
            res["price"] = float(re.findall("[0-9]+.[0-9]+", s[1])[0])

    return res


for i, data in enumerate(result):
    if i > 100:
        break
    print(parse_one(data)["isbn"])

