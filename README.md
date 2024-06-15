# Password-Generator
This program is made for those who frequently forget their passwords.
It helps you save your passwords and generate strong and safe new passwords without having to worry about forgeting them

# Instructions
1. clone repository
    ```bash
    git clone https://github.com/zgeybi/Password-Generator.git
    ```
2. ```bash 
   cd Password-Generator
   ```
3. install packages mentioned in `requirements.txt`
4. run 
    ```bash
    python3 main.py
    ```

# What's going on
## GUI
GUI is made using `customtkinter` library, which has an elegant and modern look
## Encryption of passwords
Encryption is done using `cryptography` library, specifically fernet.\
`fernet` allowed us to use symmetric encryption to be able to securely encrypt and transmit user's passwords. It uses a uniquely generated URL-safe base64-encoded 32-byte key to encrypt a string and returns a URL-safe base64-encoded message. \
The key is stored on the user's machine so there is no risk of it being stolen while transmitting the data.
## Storing cache
To simulate the work of cache, I'm using a .txt file to/from which data is being written/read, the file `cache.txt` is generated once the connection with the server is established and is deleted after the user clicks 'Save and Exit', which updates the server with new data and terminates the connection with the server

## Connection with the server
I'm using `sockets` library to connect using TCP to a linux server in the cloud. \
The `client.py` file runs on the user's side and handles data transmition between the user and the serve.

# Some instructions
## Password Generator window
Enter the name of the website you need to generate a password for and click generate. Password is written to `cache.txt`, BUT DON'T EXIT THE APP YET. \
To save new passwords in your account you MUST go back to menu and click `save and exit`.

## Password Explorer window
Here data in `cache.txt` will be read and viewed in a text box. You have the option to change some passwords to something you like. \
!IMPORTANT!
Make sure you maintain the format: \
`website-name: password\n` \
`website-name: password\n` \
This guarantees correct read/write operations to and from the database. \
DON'T EXIT THE APP YET \
when you click save, it writes new changes into `cache.txt`, to finish your session and send back the data go back to main menu and click `save and exit`.

# Notes
`main.py` is the entry file for the program. \
Also the program runs bash scripts, to make sure you get the best experience, in the meantime, make sure you have bash installed and accessible from the directory you clone the repo to.

