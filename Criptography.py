from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64
import os

def generate_key_from_password_fernet(password: str) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"alligator2",
        iterations=480000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def generate_key_from_password_aes(password: str) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 32 bytes = AES-256
        salt=b"alligator2",
        iterations=480000,
    )
    return kdf.derive(password.encode())  # ✅ raw bytes, NOT base64

def Simple_Encrypt():
    os.system("clear")
    password = input("Insert a password (leave blank for random key): ")
    if password == "":
        key = Fernet.generate_key()
        print("IMPORTANT TO SAVE THIS KEY\n" + key.decode() + "\n")
        f = Fernet(key)
    else:
        key = generate_key_from_password_fernet(password)
        f = Fernet(key)
    msg = input("Messaggio: ").encode()
    token = f.encrypt(msg)
    print(token.decode())
    leave = input("1 To go back to menu, 0 to quit program: ")
    if leave == "0":
        quit()
    elif leave == "1":
        Menu()

def Simple_Decrypt():
    os.system("clear")
    choice = input("Do you have a password (p) or a key (k)? ")
    if choice == "p":
        key = generate_key_from_password_fernet(input("Insert password: "))
    elif choice == "k":
        key = input("Paste secret key here: ").encode()
    f = Fernet(key)
    token_crypted = input("Paste message here: ").encode()
    try:
        token_decrypted = f.decrypt(token_crypted)
        print(token_decrypted.decode())
    except Exception:
        print("Wrong key or corrupted message!")
    leave = input("1 To go back to menu, 0 to quit program: ")
    if leave == "0":
        quit()
    elif leave == "1":
        Menu()

def AES_Encrypt():
    os.system("clear")
    password = input("Insert a password (leave blank for random key): ")
    if password == "":
        key = os.urandom(32)
        print("IMPORTANT TO SAVE THIS KEY\n" + base64.urlsafe_b64encode(key).decode() + "\n")
    else:
        key = generate_key_from_password_aes(password)
    iv = os.urandom(12)
    msg = input("Text: ").encode()
    encryptor = Cipher(algorithms.AES(key), modes.GCM(iv)).encryptor()
    ciphertext = encryptor.update(msg) + encryptor.finalize()
    tag = encryptor.tag
    output = iv + tag + ciphertext
    print(base64.urlsafe_b64encode(output).decode())
    leave = input("1 To go back to menu, 0 to quit program: ")
    if leave == "0":
        quit()
    elif leave == "1":
        Menu()

def AES_Decrypt():
    os.system("clear")
    choice = input("Do you have a password (p) or a key (k)? ")
    if choice == "p":
        key = generate_key_from_password_aes(input("Insert password: "))
    elif choice == "k":
        key = base64.urlsafe_b64decode(input("Paste secret key here: "))
    try:
        data = base64.urlsafe_b64decode(input("Paste message here: "))
        iv         = data[:12]
        tag        = data[12:28]
        ciphertext = data[28:]
        decryptor = Cipher(algorithms.AES(key), modes.GCM(iv, tag)).decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        print(plaintext.decode())
    except Exception:
        print("Wrong key or corrupted message!")
    leave = input("1 To go back to menu, 0 to quit program: ")
    if leave == "0":
        quit()
    elif leave == "1":
        Menu()

def Menu():
    os.system("clear")
    print("""   █████████                                  █████                 █████         
  ███▒▒▒▒▒███                                ▒▒███                 ▒▒███          
 ███     ▒▒▒  ████████  █████ ████ ████████  ███████    ██████   ███████   ██████ 
▒███         ▒▒███▒▒███▒▒███ ▒███ ▒▒███▒▒███▒▒▒███▒    ███▒▒███ ███▒▒███  ███▒▒███
▒███          ▒███ ▒▒▒  ▒███ ▒███  ▒███ ▒███  ▒███    ▒███████ ▒███ ▒███ ▒███ ▒███
▒▒███     ███ ▒███      ▒███ ▒███  ▒███ ▒███  ▒███ ███▒███▒▒▒  ▒███ ▒███ ▒███ ▒███
 ▒▒█████████  █████     ▒▒███████  ▒███████   ▒▒█████ ▒▒██████ ▒▒████████▒▒██████ 
  ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒       ▒▒▒▒▒███  ▒███▒▒▒     ▒▒▒▒▒   ▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  
                         ███ ▒███  ▒███                                           
                        ▒▒██████   █████                                          
                         ▒▒▒▒▒▒   ▒▒▒▒▒                                           """)
    print("Tool made by Edoardo")
    print("1. Simple fernet encryption")
    print("2. Simple fernet decryption")
    print("3. AES encryption")
    print("4. AES decryption")
    print("0. Quit program")
    choice = input("Input number: ")
    if choice == "0":
        quit()
    elif choice == "1":
        Simple_Encrypt()
    elif choice == "2":
        Simple_Decrypt()
    elif choice == "3":
        AES_Encrypt()
    elif choice == "4":
        AES_Decrypt()

Menu()
