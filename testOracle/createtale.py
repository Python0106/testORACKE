import pymysql

db = pymysql.connect(host='localhost',user='root',passwd='123456',db='testdb')
cursor = db.cursor()
try:
#  cursor.execute('drop table if EXISTS student')
    sql = '''
    create table student(
    sno int(8) primary key auto_increment,
    sname varchar(30) not null,
    sex varchar(5),
    age int(2),
    score float(3,1)
    )
    '''
    cursor.execute(sql)
except Exception as e:
    print(e)
    print("创建表失败")
finally:
    db.close()