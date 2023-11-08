import socket
import threading
import os


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '91.192.102.214'
port = 5000

thread_count = 0

try:
    server.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for connection')

server.listen(5)

def get_passwords(connection):
    username1 = connection.recv(1024).decode()
    connection.send(str.encode('s'))
    os.chdir(f'/home/{username1}')
    number_of_lines = connection.recv(1024).decode()
    connection.send(str.encode('s'))
    data = {}
    for i in number_of_lines:
        username = connection.recv(2048)
        connection.send(str.encode('s'))
        password = connection.recv(2048)
        connection.send(str.encode('s'))
        data[username] = password

    print(data)
    lines = []
    for j in list(data.keys()):
        lines.append(f'{j.decode()} {data[j].decode()} ')
    print(lines)
    with open(f'passwords-{username1}', 'w') as f:
        f.writelines(lines)
    

while True:
    Client, address = server.accept()
    client_handler = threading.Thread(
        target=get_passwords,
        args=(Client,)
    )
    client_handler.start()
    thread_count += 1
    print('Connection Request: ' + str(thread_count))
