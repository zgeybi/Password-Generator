from customtkinter import CTkToplevel, CTk, CTkLabel, CTkEntry, CTkButton, set_appearance_mode, set_default_color_theme
import main
import client
import menu


class LoginWindow:
    def __init__(self):
        self.root = CTk()
        self.root.title("Login")
        self.root.geometry('500x500')
        set_appearance_mode('dark')
        set_default_color_theme('green')

        # Create username fields
        self.username_label = CTkLabel(self.root, text="Username:", font=('System', 20))
        self.username_label.pack(pady=12, padx=10)
        self.username_entry = CTkEntry(self.root, font=('System', 20))
        self.username_entry.pack(pady=12, padx=10)

        # Create password fields

        self.password_label = CTkLabel(self.root, text="Password:", font=('System', 20))
        self.password_label.pack(pady=12, padx=10)
        self.password_entry = CTkEntry(self.root, show="*", font=('System', 20))
        self.password_entry.pack(pady=12, padx=10)

        # Create login button
        self.login_button = CTkButton(self.root, text="Login", command=self.login, font=('System', 20))
        self.login_button.pack(pady=12, padx=10)
        self.back_button = CTkButton(self.root, text="Back", command=self.back, font=('System', 20))
        self.back_button.pack(pady=12, padx=10)


        self.root.mainloop()

    def back(self):
        self.root.destroy()
        app = main.App()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        response = client.connect_socket(username, password, 'log')
        if response[0] == 'L1':
            dic = response[1]
            self.root.destroy()
            menu.run_menu(username, dic)
        elif response[0] == 'L0':
            self.error = CTkLabel(self.root, text='Wrong password, try again', font=('System', 20))
            self.error.pack(padx=10, pady=12)
            pass
        else:
            pass
