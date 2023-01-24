# Thread

Thread (hoặc luồng) là một khái niệm quan trọng trong lập trình hướng đối tượng và là một phần cơ bản của hầu hết các ngôn ngữ lập trình hiện đại.

Trong Python, có thể sử dụng thư viện threading để tạo và quản lý các thread. Ví dụ:

Copy code
import threading

def print_numbers():
for i in range(10):
print(i)

def print_letters():
for letter in 'abcdefghij':
print(letter)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()
Trong ví dụ trên, hai hàm print_numbers() và print_letters() được tạo ra làm hai thread riêng biệt và chạy song song.

Threads có thể sử dụng để tăng hiệu suất của chương trình bằng cách cho phép chúng chạy song song và sử dụng nhiều nhân (nếu chương trình chạy trên máy tính đa nhân).

Threads cũng có thể sử dụng để quản lý việc tải dữ liệu từ mạng, quản lý giao diện người dùng và thực hiện các tác vụ khác mà không làm chậm chương trình chính.

Trong python, có thể sử dụng thư viện concurrent.futures để quản lý thread, thay vì sử dụng thư viện threading, đi
