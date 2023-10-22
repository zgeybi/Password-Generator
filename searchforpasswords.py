import tkinter as tk
import tkinter.ttk as ttk


def lookup():
    window3 = tk.Toplevel()
    window3.geometry("500x55")
    window3.title("Search")

    search_bar = ttk.Entry(window3)
    search_bar.pack()

    window3.mainloop()
