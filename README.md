# Password-Generator
This program is made for those who frequently forget their passwords.
It helps you save your passwords and generate strong and safe new passwords without having to worry about forgeting them

# Instructions
1. clone repository
2. `cd Password-Generator`
3. run `python3 main.py`

# What's going on
Authorization and storing passwords is done on a linux server, client side is for user to edit passwords or generates new ones, then socket does the job of saving this information back to the database

# Register window
To register yourself, enter your master username and password and click register, Menu window will open

# Login window
Log in using your master username and password, Menu window will open, and a `cache.txt` file will be created, to which your saved passwords and new passwords will be written to.

# Menu
Here you can choose between generating a new password or viewing the passwords you have saved in your account.

# Password Generator window
Enter the name of the website you need to generate a password for and click generate. Password is written to `cache.txt`, BUT DON'T EXIT THE APP YET. \
To save new passwords in your account you MUST go back to menu and click `save and exit`.

# Password Explorer window
Here data in `cache.txt` will be read and viewed in a text box. You have the option to change some passwords to something you like. \
!IMPORTANT!
Make sure you maintain the format: \
`website-name: password\n` \
`website-name: password\n` \
. \
etc \
This guarantees correct read/write operations to and from the database. \
DON'T EXIT THE APP YET \
when you click save, it writes new changes into `cache.txt`, to finish your session and send back the data go back to main menu and click `save and exit`.

# Notes
`main.py` is the entry file for the program. \
Also the program runs bash scripts, to make sure you get the best experience, in the meantime, make sure you have bash installed and accessible from the directory you clone the repo to.

