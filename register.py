from customtkinter import CTkToplevel, CTk, CTkLabel, CTkEntry, CTkButton, set_appearance_mode, set_default_color_theme
import main
import client
import menu
from cryptography.fernet import Fernet as F


class RegisterWindow:
    def __init__(self):
        self.root = CTk()
        self.root.title("Register")
        self.root.geometry('500x500')
        set_appearance_mode('dark')
        set_default_color_theme('green')

        self.username_label = CTkLabel(self.root, text="Username:", font=('System', 20))
        self.username_label.pack(pady=12, padx=10)
        self.username_entry = CTkEntry(self.root, font=('System', 20))
        self.username_entry.pack(pady=12, padx=10)

        self.password_label = CTkLabel(self.root, text="Password:", font=('System', 20))
        self.password_label.pack(pady=12, padx=10)
        self.password_entry = CTkEntry(self.root, show="*", font=('System', 20))
        self.password_entry.pack(pady=12, padx=10)

        self.login_button = CTkButton(self.root, text="Register", command=self.register, font=('System', 20))
        self.login_button.pack(pady=12, padx=10)
        self.back_button = CTkButton(self.root, text="Back", command=self.back, font=('System', 20))
        self.back_button.pack(pady=12, padx=10)

        self.root.mainloop()

    def back(self):
        self.root.destroy()
        app = main.App

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        response = client.connect_socket(username, password, 'reg')
        if response == 'R1':
            dic = {}
            self.root.destroy()
            key = F.generate_key()
            with open('./file.key', 'wb')as f:
                f.write(key)
            menu.run_menu(username, dic)
        else:
            error = CTkLabel(self.root, text="Such username already exists", font=('System', 20))
            error.pack(padx=10, pady=12)

