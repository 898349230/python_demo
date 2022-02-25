#--coding:utf-8--

from pymongo import MongoClient

import random

# client = MongoClient()
client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://localhost:27017/')
db = client['test']
collection = db['mine']

# collection.drop()
# collection.save({'id':1,'name':'kaka','sex':'male'})
#
for id in range(1,10):
    name = random.choice(['steve','koby','owen','tody','rony'])
    sex = random.choice(['male','female'])
    db.user.insert({'id':id,'name':name,'sex':sex})
content = db.user.find()
for i in content:
    print (i)

client.close()