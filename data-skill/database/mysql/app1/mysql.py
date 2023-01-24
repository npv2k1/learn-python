import pymysql
conection =pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='test',
    port=3306
)
#user=input('User: ')
#password =input('Password: ')

try:
    with conection.cursor() as cursor:
        query="SELECT * FROM login"
        print(query)
        a=cursor.execute(query)

        print(cursor.fetchall())
        pass

finally:
    conection.close()