import customtkinter as ctk
from tkinter import messagebox as msg
import generator as pg


class PasswordSection:
    data = {}

    def __init__(self):
        self.window2 = ctk.CTkToplevel()
        self.window2.geometry("500x500")
        self.window2.title("Password generator")
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')

        self.label2 = ctk.CTkLabel(self.window2, text="Website name:", font=('System', 20))
        self.label2.pack()
        self.website = ctk.CTkEntry(self.window2, font=('sans-serif', 20), width=500)
        self.website.pack(padx=10, pady=12)

        self.button = ctk.CTkButton(self.window2, text="Generate Password", font=('System', 20), command=self.entry_check)
        self.button.pack(padx=10, pady=12)
        self.back_button = ctk.CTkButton(self.window2, text='Back to menu', font=('System', 20), command=self.window2.destroy)
        self.back_button.pack(padx=10, pady=12)
        self.window2.mainloop()

    def call_generator(self):
        """
            calls password generator then encrypts and writes 'website-name: password' to cache.txt
        """
        passw = pg.generator()
        print(passw.encode())
        print(self.data)
        password = ctk.CTkLabel(self.window2, text=f"Your password is: {passw}", font=('System', 20), text_color='#b82c2c')
        password.pack()
        website = self.website.get()
        with open('cache.txt', 'a') as f:
            f.write(f"{website}: {passw}")

    def entry_check(self):
        """
        Verifies entered website name, calls call_generator in case of valid entry
        """
        if self.website.get() == '':
            msg.showerror("Error", "Please enter valid website name")

        else:
            self.call_generator()


