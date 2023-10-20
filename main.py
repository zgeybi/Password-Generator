import pyinputplus as py
import os
import passwordGenerator as pwg

os.system("clear")

print("""$$$$$$$$$$$$$$$       Welcome to the password generator!      $$$$$$$$$$$$$$$$$\n
$$$$$$$$$$$$$$$     Here you can generate passwords for the   $$$$$$$$$$$$$$$$$\n
$$$$$$$$$$$$$$$     different websites you visit and save    $$$$$$$$$$$$$$$$$\n
$$$$$$$$$$$$$$$ them securely in the automatically generated  $$$$$$$$$$$$$$$$$\n
$$$$$$$$$$$$$$$                 encrypted file                $$$$$$$$$$$$$$$$$
""")

password = pwg.generator()
print(password)

