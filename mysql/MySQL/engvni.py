import pymysql
connection = pymysql.connect(host='94.237.76.21',
                             user='ndatame_TestCode',
                             password='PvN2k1testcode',
                             
                             port=3306,
                             )
print(connection)
connection.close()
# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def printP(self):
#         print(f'{self.name} \t {self.age}')
#     pass


# # menu
# print('''
# 1. Thêm data
# 2. Xuất data
# 3. Sửa data
# ''')
# x = input('option: ')
# try:
#     with connection.cursor() as cursor:
#         if x == '1':
#             print("eng-vni:  ")
#             inperson = input().split(' ')
#             sql = "INSERT INTO `eng-vni` (`eng`,`vni`) VALUES (%s,%s);"
#             cursor.execute(sql, (inperson[0], inperson[1]))
#             # commit
#             connection.commit()
#         if(x == '2'):
#             sql = "SELECT * FROM `eng-vni`"
#             result_count = cursor.execute(sql)            
#             print('Data Count: ' + str(result_count))
#             tmp = cursor.fetchall()
#             print(tmp)
#             print('id\t\tname\t\tage\t\t')
#             for i in tmp:
#                 print(f'{i[0]}\t\t{i[1]}\t\t{i[2]}')
#         if(x == '3'):
#             id = input('ID=')
#             print("Nhập tên và tuổi:  ")
#             inperson = input().split(' ')
#             sql = "UPDATE `person` SET `name`=%s, `age`=%s WHERE id=%s"
#             cursor.execute(sql, (inperson[0], int(inperson[1]), int(id)))
#             # commit
#             connection.commit()
# # to do
# finally:
#     # close connection
#     connection.close()
