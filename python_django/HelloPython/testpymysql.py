import pymysql
#连接数据库
db = pymysql.connect(host = 'localhost', user = 'root', password = 'password', db = 'demo1', port = 3306)
print(db)
cur = db.cursor()
sql = "select * from login where id = {}".format(1)
print(sql)
try :
    #查询
    cur.execute(sql)
    #查询所有数据
    results = cur.fetchall()
    #获取单条数据
    # results = cur.fetchone()
    for i  in results :
        id = i[0]
        username = i[1]
        passwrod = i[2]
        print('id:{},username:{},password:{}'.format(id, username, passwrod))

    #添加数据
    sql_insert = "insert into login(username,password) values ({},{})".format('"xiaowamg33"',666)
    print('sql_insrt:{}'.format(sql_insert))
    id  = cur.execute(sql_insert)
    print('id:{}'.format(id))
    db.commit()

    #修改
    sql_update = 'update login set username = {} where id = {}'.format('"dagege"',1)
    id_update = cur.execute(sql_update)
    print('修改的行数:{}'.format(id_update))
    db.commit()

    #删除
    sql_delete = 'delete from login where id={}'.format(2)
    id_dedete = cur.execute(sql_delete)
    print('删除的行数:{}'.format(id_dedete))
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
finally:
    db.close()

