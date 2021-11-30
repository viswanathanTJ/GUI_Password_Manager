# Python Password Manager GUI
>Note: This password manager was made as a project and is NOT intended for actual use.

## Fernet Encryption

The encryption method used in this program comes from the python library [Cryptography](https://pypi.org/project/cryptography/). This program uses Fernet and hazmat encryption methods to store sensitive data (in this case passwords) into a SQL DB.

## Hash Verification
 To authenticate the user, they are prompted to create a master password (that is also used to decrypt data) which is then added with some random shadow strings and stored using a SHA3_512 Hash Function and is verified at login. Whenever the user is prompted to verify their master password, the password they enter is added with randomly generated shadow string and compared to the hash of the stored master password and access if granted if the two hashes match.
 ```python
    ##Every hash function is in misc file
 ```
 
## Features
* All CRUD functions Working.
* All Encryptions and Decryptions working.
* Multi User Supported
* Windows, Linux, Mac, Android(Termux) Supported


###### All your Datas stored in Databases folder


# Vulnerability
As mentioned at the top, this was made as a project and not intended for actual use. Below I demonstrate what any expert hacker can accomplish by exploiting a vulnerability. Just kidding 🤪 anyone can do this. Since the files are stored locally, they can easily be deleted without needing to enter any credentials and consequently all stored passwords are gone along with other data (it is good have backup at any other location). But it is very much hard to decrypt your credentials🤟.

## Requirements
Use `pip` to install:

    pip install -r requirements.txt

OR

Activate `env` and run
    
## My Website
>Project Video also available here
[🌏 viswa2k.tk](http://viswa2k.tk/)