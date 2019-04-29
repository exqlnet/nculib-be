# 书籍收藏
### 获取所有收藏书籍

##### URL: /api/book/collect

##### Method: GET

##### 返回

```json
{
  "status": 1,
  "message": "获取成功",
  "data": [{
    "bookId": "书籍ID",
    "bookName": "书名",
    "summary": "简介",
    "author": "作者",
    "cover": "封面图片URL"
  }]
}
```


### 收藏书籍

##### URL: /api/book/collect

##### Method: post

##### 参数

```json
{
  "bookId": "int, 书籍ID"
}
``` 

##### 返回

```json
{
  "status": 1,
  "message": "收藏成功"
}
```

### 取消收藏书籍

##### URL: /api/book/collect

##### Method: delete

##### 参数

```json
{
  "bookId": "int, 书籍ID"
}
``` 

##### 返回

```json
{
  "status": 1,
  "message": "取消收藏成功"
}
```
