import pymysql


def exportdata():
    try:
        with connection.cursor() as cursor:
            query='SELECT * FROM `eng-vni`'
            a=cursor.execute(query)
            print(cursor.fetchall())
    finally:
        pass
        # close connection
        #connection.close()
def adddata(eng,vni):
    try:
        with connection.cursor() as cursor:
            query=f'INSERT INTO `eng-vni` (`id`, `eng`, `vni`) VALUES (NULL,{eng}, {vni})'
            cursor.execute(query)
            connection.commit()
    finally:
        pass
        # close connection
        #connection.close()
if __name__ == "__main__":
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='test',
                             port=3306,                             
                            )
    while(True):
        eng=input('Nhập từ tiếng anh: ')
        vni=input('Nhập từ nghĩa tiếng việt: ')
        try:
            with connection.cursor() as cursor:
                query='INSERT INTO `eng-vni` (`id`, `eng`, `vni`) VALUES (NULL,\'{}\', \'{}\')'.format(eng,vni)
                cursor.execute(query)
                connection.commit()

                query='SELECT * FROM `eng-vni`'
                a=cursor.execute(query)
                print(cursor.fetchall())
        finally:
            pass
            # close connection
            #connection.close()




    pass

