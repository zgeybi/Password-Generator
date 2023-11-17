import customtkinter as ctk
import passwordwindow as psw
import searchforpasswords as sfp
from cryptography.fernet import Fernet as F
import client


class Menu:
    username = ''

    def __init__(self, username):
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
        self.save_exit.pack(padx=10, pady=12)
        self.root.mainloop()

    def gen_pas(self):
        passwd = psw.PasswordSection()

    def view_pass(self):
        view = sfp.PasswordLookup(self.username)

    def save_passwords(self):
        """
        Calls client.exit() to send back new data to server and exits back to Login/Reg window
        """
        client.exit(self.username)
        self.root.destroy()


def run_menu(username):
    men = Menu(username)

