import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    database='pythondecember',
    auth_plugin='mysql_native_password'
)

cursor=db.cursor()
sql="select * from movie"
cursor.execute(sql)
movies=cursor.fetchall()
for movie in movies:
    print(movie)