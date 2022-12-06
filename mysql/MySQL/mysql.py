from sys import argv
import os
import pymysql
connection = pymysql.connect(host='94.237.76.21',
                             user='ndatame_TestCode',
                             password='',
                             db='ndatame_testcode',
                             port=3306,
                             )


print(connection)
argv.remove('mysql.py')
ls = ' '.join(argv)
as1 = ls.split('.')
eng = as1[0]
vni = as1[1]
option=as1[2]
print(eng)
print(vni)
print(option)
# # menu
print('''
1. Thêm data
2. Xuất data
3. Sửa data
''')
x =option#input('option: ')
try:
    with connection.cursor() as cursor:
        if x == '1':
            print("eng-vni:  ")
            #inperson = input().split(' ')
            sql = "INSERT INTO `test` (`eng`,`vni`) VALUES (%s,%s);"
            cursor.execute(sql, (eng, vni))
            # commit
            connection.commit()
        if(x == '2'):
            sql = "SELECT * FROM `test`"
            result_count = cursor.execute(sql)
            print('Data Count: ' + str(result_count))
            tmp = cursor.fetchall()
            print(tmp)
            print('id\t\teng\t\tvni\t\t')
            for i in tmp:
                print(f'{i[0]}\t\t{i[1]}\t\t{i[2]}')
        if(x == '3'):
            id = input('ID=')
            print("Nhập tên và tuổi:  ")
            #inperson = input().split(' ')
            sql = "UPDATE `person` SET `eng`=%s, `vni`=%s WHERE id=%s"
            cursor.execute(sql, (eng, vni, int(id)))
            # commit
            connection.commit()
# to do
finally:
    # close connection
    connection.close()
