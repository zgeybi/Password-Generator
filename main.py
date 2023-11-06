import customtkinter as ctk
import register
import login


class App:
    def __init__(self):
        """
        constructor of authorization window
        """
        self.root = ctk.CTk()
        self.root.geometry('500x500')
        self.root.title("Main Menu")
        self.window = ctk.CTkFrame(self.root)
        self.window.pack(fill='both', expand=True)
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')

        self.label = ctk.CTkLabel(self.window, text="Please register or login to start", font=('System', 20))
        self.label.pack(pady=12, padx=10)

        self.button1 = ctk.CTkButton(self.window, text='Register', command=self.regist, font=('System', 20))
        self.button1.pack(pady=12, padx=10)

        self.button2 = ctk.CTkButton(self.window, text='Login', command=self.log, font=('System', 20))
        self.button2.pack(pady=12, padx=10)

        self.root.mainloop()

    def regist(self):
        reg = register.RegisterWindow()

    def log(self):
        auth = login.LoginWindow()


if __name__ == '__main__':
    app = App()

