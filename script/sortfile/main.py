#đây là script python hỗ trợ lọc các file trong 1 folder

#Nhập thư viện
import os
import shutil

#Lọc các têp. Khi cần thêm loại nào thì sửa như mẫu
list_dir=os.listdir() #Lấy thư mục và file ở folder hiện tại

folder_type = {
    "Compressed": ['zip','rar'],
    "Picture": ['jpg','png'],
    "Video": ['mp4'],
    "Programs": ['exe'],
    "Documents": ['doc', 'pdf','xlsx','docx','txt']
}


print(folder_type.keys())

# #cac folder. tạo folder nếu chưa có
for i in folder_type.keys():
    if(os.path.exists(os.path.join(os.getcwd(), i))):
        pass
    else:
        os.mkdir(os.path.join(os.getcwd(), i))

print(list_dir)


for file in list_dir:
    if(file == 'main.py'): continue
    if (os.path.isfile(os.path.join(os.getcwd(), file))):
        file_extension=file.split('.')[-1]
        for (k,v) in folder_type.items():        
            if file_extension in v: 
                try:
                    shutil.move(os.path.join(os.getcwd(), file), os.path.join(os.getcwd(), k,file))
                finally: 
                    pass
