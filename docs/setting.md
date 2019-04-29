# 推荐书籍的学科设置


### 获取学科选项
##### URL: /api/book/subject/setting
##### Method: GET
##### 返回

```json
{
  "status": 1,
  "message": "获取成功",
  "data": [{
    "subjectId": "学科ID",
    "subjectName": "学科名"
  }]
}
```


### 获取自己设置的学科
##### URL: /api/book/subject/info
##### Method: GET
##### 返回

```json
{
  "status": 1,
  "message": "获取成功",
  "data": [{
    "subjectId": "int, 学科ID",
    "subjectName": "str, 学科名称",
    "checked": "bool, 是否设置"
  }] 
}
```


### 设置学科
##### URL: /api/book/subject/info
##### put: Method: PUT
##### 参数

```json
{
  "subjects": ["int, 学科ID列表"]
}
```

##### 返回

```json
// 成功
{
  "status": 1,
  "message": "设置成功"
}
```

```json
// 因部分ID无法在数据库中找到而导致错误
{
  "status": 0,
  "message": "提交有误"
}
```
