import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root@10.175.134.107", "Rejy9aWo", "airflow")

# 使用cursor()方法创建一个游标对象 cursor
cursor = db.cursor()


# 数据库查询操作
# Python查询MySQL使用fetchone()方法获取单条数据，使用fetchall()方法获取多条数据
# SQL查询语句
sql = "select * from task_instance"

try:
    # 执行sql语句
    cursor.execute(sql)
    # 获取所有记录列表
    ret = cursor.fetchall()
    print(ret)
except:
    print("ERROR: unable to fetch data")

# 关闭数据库连接
cursor.close()


