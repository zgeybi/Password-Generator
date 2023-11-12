import customtkinter as ctk


class PasswordLookup:
    def __init__(self, username):
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
        with open('cache.txt', 'r') as f:
            lines = f.readlines()
        for i in lines:
            i = i.strip()
            i = i.split(': ')
            self.text.insert(index='end', text=f"{i[0]}: {i[1]}\n")
        self.window.configure(command=self.text.yview)
        self.save_btn = ctk.CTkButton(self.root, text='Save', font=('System', 16), command=self.save)
        self.save_btn.pack(padx=10, pady=12)

        self.root.mainloop()

    def save(self):
        """
        reads updated passwords from text box, and writes data into 'cache.txt' and closes window
        """
        data = self.text.get(index1='1.0', index2='end')
        print(data)
        data = data.split('\n')
        new_data = []
        for i in data:
            print(i)
            i = i.strip()
            if not i:
                pass
            else:
                new_data.append(i + '\n')
        with open('cache.txt', 'w') as f:
            f.writelines(new_data)

        self.root.destroy()

