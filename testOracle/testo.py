import sqlite3
con = sqlite3.connect("E:/sqlitedb/frist.db")
cur = con.cursor()
'''sql = 'create table tt_person(pno INTEGER PRIMARY KEY AUTOINCREMENT,pname '\
    'varchar(30) NOT NULL,age INTEGER )'''
sql = 'insert into tt_person(pname,age) values(?,?)'


try:
    cur.execute(sql,('张三',23))
    con.commit()
    print("插入成功")
except Exception as e:
    print(e)
    print("创建表失败")
finally:
    cur.close()
    con.close()


