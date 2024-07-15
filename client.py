import socket
import os
from cryptography.fernet import Fernet as F


def connect_socket(username, password, auth):
    """
        Connects client to server, sends username=master username, password=master password, auth= type of authentication
        log/reg

        in case of successful authentication, decrypts received data and writes it into 'cache.txt'
        :returns:
        tuple(response code from server, username)
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(('localhost', 5000))

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
            print("n = 1")
            with open("cache.txt", "x") as f:
                pass
            client.close()
            return response, {}, username, password
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
            with open('file.key', 'rb') as f:
                key = f.read()
            fernet = F(key)
            temporary_list = []
            for i, j in dic.items():
                i = str(fernet.decrypt(i), 'utf-8')
                j = str(fernet.decrypt(j), 'utf-8')
                temporary_list.append(f"{i}: {j}")
            print(temporary_list)
            with open('cache.txt', 'w+') as f:
                f.writelines(temporary_list)

        return response, username
    else:
        client.send(str.encode(username))
        client.recv(1024)
        client.send(str.encode(password))
        response = client.recv(1024).decode()
        client.close()
        with open('cache.txt', 'x') as f:
            pass
        return response


def exit(username):
    """
        Reads 'cache.txt', encrypts credentials, and sends the information back to server
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5050))
    client.send(str.encode(username))
    client.recv(1024)
    with open('file.key', 'rb') as f:
        key = f.read()
    fernet = F(key)
    with open('cache.txt', 'r') as f:
        lines = f.readlines()
    new_lines = []
    for i in lines:
        i = i.split(': ')
        print(i)
        encrypted_username = fernet.encrypt(i[0].encode())
        encrypted_website = fernet.encrypt(i[1].encode())
        new_lines.append(encrypted_username)
        new_lines.append(encrypted_website)
    client.send(str.encode('*' * len(lines)))
    client.recv(1024)
    for i in range(0, len(new_lines), 2):
        client.send(new_lines[i])
        client.recv(1024)
        client.send(new_lines[i + 1])
        client.recv(1024)
    os.system('rm cache.txt')
    client.close()

