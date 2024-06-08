import socket


host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Server listened at {host}:{port}")

conn, addr = server_socket.accept()
print(f"Connect from {addr}")

with open('file2.txt', 'wb') as file:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        file.write(data)

print("success!")
conn.close()