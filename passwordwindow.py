import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as msg
import generator as pg

passw = ''


def password_section():

    def call_generator():
        global passw
        passw = pg.generator()
        print(passw)
        password = ttk.Label(window2, text=f"Your password is: {passw}")
        password.pack()
        with open("passwords.txt", "a") as f:
            f.write(f"username: {username.get()}, website: {website.get()}, password: {passw}")

    def entry_check():
        if username.get() == '' or website.get() == '':
            msg.showerror("Error", "Please enter valid username and website name")

        else:
            call_generator()

    global passw
    window2 = tk.Toplevel()
    window2.geometry("500x500")
    window2.title("Password generator")

    label = ttk.Label(window2, text="Username: ")
    label.pack()
    username = ttk.Entry(window2)
    username.pack()
    label2 = ttk.Label(window2, text="Website: ")
    label2.pack()
    website = ttk.Entry(window2)
    website.pack()

    button = ttk.Button(window2, text="Generate Password", width=25, padding=5, command=entry_check)
    button.pack()

    window2.mainloop()

