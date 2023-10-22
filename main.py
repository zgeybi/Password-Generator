import pyinputplus as py
import os
import tkinter as tk
import tkinter.ttk as ttk
import passwordwindow
import searchforpasswords


def main():
    window = tk.Tk()
    window.title("Main Menu")
    window.geometry("500x500")

    label1 = ttk.Label(text="Password generator", padding=7)
    label1.grid(column=0, row=0, sticky='W', pady=2, padx=5)
    label1.grid_rowconfigure(index=0, weight=3, minsize=100)
    label1.grid_columnconfigure(index=0, weight=3, minsize=100)
    generator_page = ttk.Button(text="Password generator", command=passwordwindow.password_section)
    generator_page.grid(column=1, row=0, columnspan=2, pady=2, sticky='E', padx=5)
    label2 = ttk.Label(text="Find password", padding=7)
    label2.grid(row=1, column=0, pady=2, padx=5)
    password_finder_page = ttk.Button(text="Find password", command=searchforpasswords.lookup)
    password_finder_page.grid(row=1, column=1, columnspan=2, pady=2, padx=5)

    window.mainloop()


if os.path.exists('./passwords.txt'):
    main()
else:
    os.system('touch passwords.txt')
    main()
