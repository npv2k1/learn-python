import random
'''
1=kéo
2=búa
3=bao
'''

print('''1: kéo
2: búa
3: bao''')
user_Select=int(input("mời bạn lựa chọn: "))
listdc={
    1: 'Kéo',
    2: 'Búa',
    3: 'Bao',
}
pc_Select=random.randint(1,3)

if(user_Select==1 and pc_Select==2):
    print(listdc.get(1) +'+'+listdc.get(2))
    print("Bạn thua")
elif(user_Select==2 and pc_Select == 3):
    print(listdc.get(2) + '+' + listdc.get(3))
    print('Bạn thua')
elif(user_Select==3 and pc_Select==1):
    print(listdc.get(3) + '+' + listdc.get(1))
    print('Bạn thua')
elif(user_Select==pc_Select):
    print(listdc.get(user_Select) + '+' + listdc.get(pc_Select))
    print("Hòa")
else:
    print(listdc.get(user_Select) + '+' + listdc.get(pc_Select))
    print("Bạn thắng")
