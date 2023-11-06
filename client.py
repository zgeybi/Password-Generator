import socket
import os


def connect_socket(username, password, auth):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(('91.192.102.214', 5050))

    client.send(str.encode(auth))
    client.recv(1024)
    if auth == 'log':
        client.send(str.encode(username))
        client.recv(1024)
        client.send(str.encode(password))
        response = client.recv(1024)
        response = response.decode()
        client.send(str.encode('s'))
        n = client.recv(2048).decode()
        if n == '1':
            client.close()
            return response, username, password
        else:
            client.send(str.encode('s'))
            dic = {}
            for i in n:
                username = client.recv(1024).decode()
                client.send(str.encode('s'))
                password = client.recv(1024).decode()
                client.send(str.encode('s'))
                dic[username] = password

            client.close()
        return response, dic, username, password
    else:
        client.send(str.encode(username))
        client.recv(1024)
        client.send(str.encode(password))
        response = client.recv(1024).decode()
        client.close()
        return response


def exit(username):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('91.192.102.214', 5000))
    client.send(str.encode(username))
    client.recv(1024)
    with open('temp.txt', 'r') as f:
        lines = f.readlines()
    client.send(str.encode('*' * len(lines)))
    client.recv(1024)
    for i in lines:
        client.send(str.encode(i.split()[0]))
        client.recv(1024)
        client.send(str.encode(i.split()[1]))
        client.recv(1024)
    os.system('rm temp.txt')
    client.close()

