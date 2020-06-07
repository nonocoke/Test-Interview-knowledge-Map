#! /usr/bin/python3

import pymongo

# 连接本地数据库
db_client = pymongo.MongoClient("mongodb://localhost:27017/")
# 切换到 testdb 测试数据库
test_db = db_client["testdb"]
# 切换到 sites 文档
site_obj = test_db["sites"]
# find_one() 方法查询集合中的一条数据
first_data = site_obj.find_one()
print("py mongo test:")
print(first_data)
