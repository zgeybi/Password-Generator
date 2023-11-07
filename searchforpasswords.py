import customtkinter as ctk
import client
from cryptography.fernet import Fernet as F


class PasswordLookup:
    def __init__(self, data, username):
        self.username = username
        self.root = ctk.CTk()
        self.root.geometry('500x500')
        self.root.title('Password Explorer')
        self.window = ctk.CTkScrollbar(self.root)
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')
        self.window.pack(side='right', fill='y')

        self.text = ctk.CTkTextbox(self.root, font=('system', 16), width=self.root.winfo_width(), yscrollcommand=self.window.set)
        self.text.pack(side='top', fil='x')
        decrypted_data = self.decrypt_data(data)
        for i in decrypted_data.items():
            self.text.insert(index='end', text=f"{i[0]}: {i[1]}\n")
        self.window.configure(command=self.text.yview)
        self.save_btn = ctk.CTkButton(self.root, text='Save', font=('System', 16), command=self.save)
        self.save_btn.pack(padx=10, pady=12)

        self.root.mainloop()

    def decrypt_data(self, data):
        with open('file.key', 'rb') as f:
            key = f.read()
        fernet = F(key)
        decrypted_data = {}
        for i, j in data.items():
            i = str(fernet.decrypt(i), 'utf-8')
            decrypted_data[i] = str(fernet.decrypt(j), 'utf-8')
        return decrypted_data

    def save(self):
        data = self.text.get(index1='1.0', index2='end').split('\n')
        print(data)
        new_data = {}
        for i in data:
            if i == '':
                break
            line = i.split(': ')
            new_data[line[0]] = line[1]
        with open('file.key', 'rb') as f:
            key = f.read()

        fernet = F(key)
        new_dict = {}
        for i in list(new_data):
            temp = i
            i = fernet.encrypt(bytes(i, 'utf-8'))
            new_dict[i] = fernet.encrypt(bytes(new_data[temp], 'utf-8'))
        print(new_data)
        print(new_dict)
        with open('temp.txt', 'w') as f:
            for i in list(new_dict):
                f.write(i.decode() + ' ' + new_dict[i].decode() + '\n')
        client.exit(self.username)
        self.root.destroy()

