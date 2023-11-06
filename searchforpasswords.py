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
        for i in data.items():
            self.text.insert(index='end', text=f"{i[0]}: {i[1]}\n")
        self.window.configure(command=self.text.yview)
        self.save_btn = ctk.CTkButton(self.root, text='Save', command=self.save)
        self.save_btn.pack(padx=10, pady=12)

        self.root.mainloop()

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
        for i, j in new_data.items():
            new_data[i] = fernet.encrypt(bytes(j, 'utf-8'))

        with open('temp.txt', 'w') as f:
            for i in new_data.items():
                f.write(f'{i[0]} {i[1]}')
        print(self.username)
        client.exit(self.username)

