import socket
import os
import threading
import hashlib


ServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
host = 'localhost'
port = 5000
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)
HashTable = {}

with open('/home/tim/server/users.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        pair = i.split()
        HashTable[pair[0]] = pair[1]

def threaded_client(connection):
    auth = connection.recv(1024)
    auth = auth.decode()
    connection.send(str.encode('s'))
    if auth == 'reg':
        name = connection.recv(2048)
        connection.send(str.encode('s'))
        password = connection.recv(2048)
        password = password.decode()
        name = name.decode()
        password = hashlib.sha256(str.encode(password)).hexdigest()
        if name not in HashTable:
            HashTable[name] = password
            connection.send(str.encode('R1'))
            os.mkdir(f'/home/tim/users/{name}')
            os.chdir(f'/home/tim/users/{name}')
            os.system(f'touch passwords-{name}')
            print('Registered : ', name)
            print("{:<8} {:<20}".format('USER', 'PASSWORD'))
            for k, v in HashTable.items():
                label, num = k, v
                print("{:<8} {:<20}".format(label, num))
            print("-------------------------------------------")
        else:
            print(f'Username {name} already exists')
            connection.send(str.encode('R0'))

    elif auth == 'log': 
        name = connection.recv(1024)
        connection.send(str.encode('s'))
        password = connection.recv(1024)
        password = password.decode()
        name = name.decode()
        password = hashlib.sha256(str.encode(password)).hexdigest()

        if name not in HashTable:
            connection.send(str.encode("L2"))

        else:
            if (HashTable[name] == password):
                connection.send(str.encode('L1'))
                os.chdir(f'/home/tim/users/{name}')
                connection.recv(1024)
                with open(f'passwords-{name}', 'r') as f:
                    lines = f.read()
                if len(lines) == 0: 
                    print('Connected : ', name)
                    connection.send(str.encode('1'))
                else:
                    print(len(lines.split())//2)
                    connection.send(str.encode('*' * (len(lines.split())//2)))
                    connection.recv(1024)
                    lines = lines.split()
                    print(lines)
                    print(len(lines))
                    for i in range(0, len(lines), 2):
                        connection.send(lines[i].encode())
                        connection.recv(1024)
                        connection.send(lines[i+1].encode())
                        connection.recv(1024)
                    print('Connected : ', name)
            else:
                connection.send(str.encode('L0'))
                print('Connection denied : ', name)
    while True:
        break
    with open('/home/tim/server/users.txt', 'w') as file:
        for i in HashTable.items():
            file.write(f"{i[0]} {i[1]}\n")

    connection.close()


while True:
    Client, address = ServerSocket.accept()
    client_handler = threading.Thread(
        target=threaded_client,
        args=(Client,)
    )
    client_handler.start()
    ThreadCount += 1
    print('Connection Request: ' + str(ThreadCount))

ServerSocket.close()
