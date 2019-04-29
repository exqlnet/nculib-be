from app import db
from datetime import datetime, date
from decimal import Decimal


def to_dic(sql, params=None, name_list=None):

    try:
        data = db.session.execute(sql, params).fetchall()
    except Exception as e:
        # print(e)
        return []
    result = list()
    if not name_list is None:
        for row in data:
            i = 0
            dic = dict()
            for name in name_list:
                if isinstance(row[i], datetime):
                    dic[name] = row[i].strftime('%Y-%m-%d %H:%M:%S')
                elif isinstance(row[i], date):
                    dic[name] = row[i].strftime('%Y-%m-%d')
                elif isinstance(row[i], Decimal):
                    dic[name] = float(row[i])
                else:
                    dic[name] = row[i]
                i = i + 1
            result.append(dic)
    else:
        for row in data:
            dic = dict()
            for i in range(data.rowcount):
                dic[i] = row[i]
            result.append(dic)
    return result
