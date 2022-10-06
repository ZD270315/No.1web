import pymysql


conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password="judy270315",
        db='personinfo',
    )
cursor = conn.cursor()

cursor.execute("insert into persons( name, password, mobile) values('jinduo','999999','13366669999')")
conn.commit()

# 关闭
cursor.close()
conn.close()


