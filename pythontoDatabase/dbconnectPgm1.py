import mysql.connector #step 1:import mysql connector

#Step2:establish a connection with mysql
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password'
)

#step3:create a cursor object
cursor=db.cursor()
sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)
db.close()
