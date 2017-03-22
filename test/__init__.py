import scipy as sp
import stockstats as ss
import pymysql as psql
import GlobalLib.Genv as env

# 打开数据库连接
#db = psql.connect("localhost", "root", "benson1234", "TEST")
db = psql.connect("localhost",env.g_dbUser , env.g_dbPWD, env.g_dbName)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute() 方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据
# data = cursor.fetchone()
# print ("Database version : %s " % data)

sql = "select * from employee"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % (fname, lname, age, sex, income))

except:
    print("error!!!")

# 关闭数据库连接
db.close()
