#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

db = client['python']

collection = db['students']

student1 = {
    'id': '20170101',
    'name': 'jordan',
    'age': '20',
    'gender': 'male'
}
student2 = {
    'id': '20170102',
    'name': 'jery',
    'age': '21',
    'gender': 'male'
}

#insert插入
result=collection.insert([student1,student2])
#result=collection.insert_many([student1,student2])

# print(result)
# print(result.inserted_ids)
# print(result)

# 查询  find_one查询单条
# result=collection.find_one({'name':'jery'})

# find 返回多条 为Cursor类型
# results=collection.find({'name':'jery'})
# for result in results:
#     print(result)

# 查询年龄大于20的数据
# results=collection.find({'age':{'$gt':19}})
# for result in results:
#     print(result)

# 排序
# results=collection.find().sort('name',pymongo.ASCENDING)
# print([result['name'] for  result in results])

# 偏移  skip 忽略前几个元素
# results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
# print([result['name'] for result in results])

# 更新  update  update_many update_one
# condition = {'name': 'jordan'}
# student=collection.find_one(condition)
# student['age']=25
# result=collection.update(condition,student)
# print(result)

# 查询到条件的数据值加1
# result=collection.update_one(condition,{'$inc':{'age':1}})
# print(result)
# print(result.matched_count,result.modified_count)