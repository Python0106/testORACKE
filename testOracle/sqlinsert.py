import sqlite3

con = sqlite3.connect("e:/sqlitedb/frist.db")
cur = con.cursor()
try:
    '''sql = 'insert into tt_person(pname,age)values(?,?)'
    cur.executemany(sql,[('张三',14),('李四',16),('王二',19)])
    con.commit()'''
    sql = 'update tt_person set pname=? where pno=?'
    cur.execute(sql,('丈八',1))
    con.commit()
    sql1 = 'select * from tt_person'
    cur.execute(sql1)
    print('修改成功')
    cha_all = cur.fetchall()
    for a in cha_all:
        print(a)
except Exception as e:
    print(e)
    print("修改失败")
    con.rollback()
finally:
    cur.close()
    con.close()
