#! /usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect('localhost', 'user', 'pw', 'testdb', charset='utf-8')
# 使用 cursor() 获取操作游标
_cursor = db.cursor()
# 使用 execute 方法执行 SQL 语句
_cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取一条数据
data = _cursor.fetchone()
# 关闭数据库连接
db.close()
