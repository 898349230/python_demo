#coding=utf-8

from pymongo import MongoClient
import random

client = MongoClient("localhost", 27017)
# test : 数据库名称
db = client['test']
# person ：数据库下的 collection 名称
content = db.person.find()
for id in range(1, 10):
    name = random.choice(['tim', 'david', 'jenny', 'tom', 'jerry'])
    sex = random.choice(['male', 'female'])
    db.person.insert({'id': id, 'name': name, 'sex': sex})
content2 = db.person.find()
for i in content2:
    print (i)
print ("######################################")
for j in content:
    print (j)
print ("+++++++++++++++++++++++++++++++++")
content3 = db.test.find()
for i in content3:
    print (i)
client.close()