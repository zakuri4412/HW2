import socket
host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

file_path = 'file.txt'

with open(file_path, 'rb') as file:
    data = file.read()
    client_socket.sendall(data)

print("Send success!")
client_socket.close()