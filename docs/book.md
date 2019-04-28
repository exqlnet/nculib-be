# 图书接口

### 查询图书

##### URL: /api/book/query

##### Method: GET

##### 参数

```json
{
  "key": "str, 关键词",
  "fulltext": "bool&optional, 是否全文搜索",
  "page": "int&default=1, 第几页",
  "per_page": "int&default=20, 每页多少条"
}
```

##### 返回

```json
{
  "status": 1,
  "message": "获取成功",
  "total_page": "int, 结果总共几页",
  "data": [{
    "bookId": "书籍ID",
    "bookName": "书名",
    "pressTime": "发行时间",
    "isbn": "isbn",
    "classification": "中法图书号",
    "totalPage": "本书总页数",
    "summary": "简介"
  }]
}
```

### 获取推荐

##### URL: /api/book/recommend

##### Method: GET

##### 返回

```json
{
  "status": 1,
  "message": "获取成功",
  "total_page": "int, 结果总共几页",
  "data": [{
    "bookId": "书籍ID",
    "bookName": "书名",
    "pressTime": "发行时间",
    "isbn": "isbn",
    "classification": "中法图书号",
    "totalPage": "本书总页数",
    "summary": "简介",
    "press": "出版社",
    "author": "作者",
    "cover": "封面图片URL"
  }]
}
```

