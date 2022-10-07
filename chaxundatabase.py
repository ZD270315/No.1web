import pymysql

# 连接数据库
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password="judy270315",
    db='personinfo',
)
cursor = conn.cursor()

# 使用sql语句不可以用占位符
'''
cursor.execute("insert into persons( name, password, mobile) values('牛阿包','3333','13333669999')")
conn.commit()
'''
'''
sql = "insert into persons( name, password, mobile) values(%s,%s,%s)"
cursor.execute(sql, ["王兰", "3399", "16666339966"])
conn.commit()
'''

'''
sql = "insert into persons( name, password, mobile) values(%(n1)s,%(n2)s,%(n3)s)"
cursor.execute(sql, {"n1" : "李小璐", "n2" : "9966", "n3" : "13366999996"})
conn.commit()
'''
cursor.execute("select * from personinfo.persons where id > %s", [2, ])
data_list = cursor.fetchall()
for row_dict in data_list:
    print(row_dict)

# 关闭
cursor.close()
conn.close()
