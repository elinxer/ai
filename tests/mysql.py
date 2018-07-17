"""

mysql connection

测试通过实例
Python 3.6
package pymysql

"""

import pymysql.cursors

connect = pymysql.Connect(
    host='121.199.14.161',
    port=3306,
    user='yangdongsheng',
    passwd='OkLKAScG',
    db='flowertown',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()

sql = "select * from users where id ='%s'"
data = ('1',)

cursor.execute(sql % data)

# 查询数据
for row in cursor.fetchall():
    print(row)
    pass

print('共查找出', cursor.rowcount, '条数据')

# 关闭连接
cursor.close()
