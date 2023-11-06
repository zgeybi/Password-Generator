import customtkinter as ctk
import passwordwindow as psw
import searchforpasswords as sfp
from cryptography.fernet import Fernet as F
import client


class Menu:
    username = ''
    data = {}

    def __init__(self, username, dic):
        """
        constructor of main menu, username: master username, dic: dictionary of {usernames:passwords}
        """
        self.data = dic
        self.username = username
        self.root = ctk.CTk()
        self.root.geometry('600x600')
        self.root.title('Menu')
        self.window = ctk.CTkFrame(self.root)
        self.window.pack(fill='both', expand=True)
        ctk.set_default_color_theme('green')
        ctk.set_appearance_mode('dark')

        self.label = ctk.CTkLabel(self.window, text='Generate new password or view passwords: ', font=('System', 20))
        self.label.pack(padx=10, pady=12)

        self.generate_button = ctk.CTkButton(self.window, text='Generate Password', font=('System', 20), command=self.gen_pas)
        self.generate_button.pack(padx=10, pady=12)

        self.view_pass = ctk.CTkButton(self.window, text='View Passwords', font=('System', 20), command=self.view_pass)
        self.view_pass.pack(padx=10, pady=12)

        self.save_exit = ctk.CTkButton(self.window, text='Save and Exit', font=('System', 20), command=self.save_passwords)

        self.root.mainloop()

    def gen_pas(self):
        passwd = psw.PasswordSection(self.data)

    def view_pass(self):
        view = sfp.PasswordLookup(self.data, self.username)

    def save_passwords(self):
        """
        encrypts newly generated passwords and prepares it for sending back to host for storage
        calls client.exit which sends back new data
        """
        with open('file.key', 'rb') as f:
            key = f.read()

        fernet = F(key)
        for i in self.data.items():
            encrypted = fernet.encrypt(bytes(i[1], 'utf-8'))
            i[1] = encrypted
        with open('temp.txt', 'w') as f:
            for i in self.data.items:
                f.write(f'{i[0]} {str(i[1])}')
        client.exit(self.username)


def run_menu(username, data):
    men = Menu(username, data)

