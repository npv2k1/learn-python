print("mời bạn nhập tên: ", end="")
tin = input()
def cht(tin):
    temp1 = tin.split() #nhận tên và chuyển thành list
    temp2 = []
    #lấy các phần tủ củ list trên xử lí
    for j in temp1:
        ten = ''
        for i in j: #xủ lí chuỗi
            if i.isalpha():
                ten = ten + i
        ten = ten.lower()
        ten = ten.capitalize()
        if ten.isalpha():
            temp2.append(ten)
            tout=' '.join(temp2)
    return tout
tout=cht(tin)
print(tout)