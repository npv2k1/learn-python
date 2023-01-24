# Input/Output

Trong Python, có nhiều cách để thực hiện đầu vào/đầu ra (I/O) với các dữ liệu khác nhau.

Đầu vào từ bàn phím: Sử dụng hàm input() để nhận đầu vào từ người dùng từ bàn phím. Ví dụ:
Copy code
name = input("What is your name? ")
print("Hello, " + name + "!")
Đầu ra ra màn hình: Sử dụng hàm print() để in ra màn hình. Ví dụ:
Copy code
x = 5
print("The value of x is", x)
Đọc và ghi tập tin: Sử dụng các hàm open(), read(), write() và close() để đọc và ghi tập tin. Ví dụ:
Copy code
# Đọc tập tin
f = open("example.txt", "r")
print(f.read())
f.close()

# Ghi tập tin
f = open("example.txt", "w")
f.write("Hello, world!")
f.close()
Các hàm đầu vào/đầu ra khác cũng có sẵn trong Python, chẳng hạn như pickle để lưu trữ và truy xuất dữ liệu đã được mã hóa, và csv để đọc và ghi dữ liệu tập tin CSV.