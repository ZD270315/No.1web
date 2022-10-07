from flask import Flask, render_template, request
import pymysql
app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/add/user', methods=['GET', 'POST'])
def add_user():
    if request.method == "GET":
        return render_template("adduser.html")

    username = request.form.get("user")
    password = request.form.get("pwd")
    mobile = request.form.get("mobile")
    # 连接数据库
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password="judy270315",
        db='personinfo',
    )
    cursor = conn.cursor()
    # 执行sql
    sql = "insert into persons( name, password, mobile) values(%s,%s,%s)"
    cursor.execute(sql, [username, password, mobile])
    conn.commit()
    # 关闭数据库
    cursor.close()
    conn.close()

    return "添加成功"

'''
@app.route('/add/user', methods=['GET', 'POST'])
def add_user():
    if request.method == "GET":
        return render_template("adduser.html")
    username = request.form.get("user")
    password = request.form.get("pwd")
    mobile = request.form.get("mobile")
    # 连接数据库
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password="judy270315",
        db='personinfo',
    )
    cursor = conn.cursor()
    # 执行sql
    sql = "insert into persons( name, password, mobile) values(%s,%s,%s)"
    cursor.execute(sql, [username, password, mobile])
    conn.commit()
    # 关闭数据库
    cursor.close()
    conn.close()

    return "添加成功"
'''

@app.route('/show/user', methods=['GET', 'POST'])
def show_user():
    
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password="judy270315",
        db='personinfo',
    )
    cursor = conn.cursor()
    sql = "select * from persons"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    cursor.close()
    conn.close()
    print(data_list)
    return render_template("showuser.html", data_list=data_list)


if __name__ == '__main__':
    app.run(debug=True)
