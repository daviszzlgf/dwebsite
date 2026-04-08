from flask import Flask,render_template
import pymysql
import pymysql.cursors

app = Flask(__name__)

# 数据库连接配置
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',          # 替换为你的MySQL用户名
    'password': '123456', # 替换为你的MySQL密码
    'database': 'myweb_db',    # 替换为你创建的数据库名
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

@app.route('/')
def hello():
    return '<h1>Hello, 我的Web服务器!</h1><p>如果数据库连接成功，请访问 /db-test 路径</p>'

@app.route('/db-test')
def db_test():
    try:
        # 尝试连接数据库
        connection = pymysql.connect(**config)
        return '数据库连接成功！'
    except Exception as e:
        return f'数据库连接失败：{str(e)}'

if __name__ == '__main__':
    app.run(debug=True)