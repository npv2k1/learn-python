import socket



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1",8000))
s.listen(2)

while True:
    client, addr = s.accept()
    try:
        print('Connected by', addr)
        while True:
            data = client.recv(1024)
            str_data = data.decode("utf8")
            if str_data == "quit":
                break
            if not data:
                break
            print("Client: " + str_data)

            msg = input("Server: ")
            client.sendall(bytes(msg,"utf8"))

    finally:
        client.close()

s.close()
