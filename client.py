import socket
import os


def connect_socket(username, password, auth):
    """
    Connects client to server, sends username=master username, password=master password, auth= type of authentication
    log/reg
    returns response from server as tuple
    """
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
            print(n)
            for i in n:
                username = client.recv(2048)
                print(type(username))
                print(username)
                client.send(str.encode('s'))
                password = client.recv(2048)
                print(type(password))
                print(password)
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
    """
    sends updated passwords back to server and closes connection with server
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('91.192.102.214', 5000))
    client.send(str.encode(username))
    client.recv(1024)
    with open('temp.txt', 'r') as f:
        lines = f.readlines()
    client.send(str.encode('*' * len(lines)))
    client.recv(1024)
    for i in lines:
        client.send(i.split()[0].encode())
        client.recv(1024)
        client.send(i.split()[1].encode())
        client.recv(1024)
    os.system('rm temp.txt')
    client.close()

