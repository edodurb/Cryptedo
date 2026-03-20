<div align="center">
<pre>
   █████████                                  █████                 █████         
  ███▒▒▒▒▒███                                ▒▒███                 ▒▒███          
 ███     ▒▒▒  ████████  █████ ████ ████████  ███████    ██████   ███████   ██████ 
▒███         ▒▒███▒▒███▒▒███ ▒███ ▒▒███▒▒███▒▒▒███▒    ███▒▒███ ███▒▒███  ███▒▒███
▒███          ▒███ ▒▒▒  ▒███ ▒███  ▒███ ▒███  ▒███    ▒███████ ▒███ ▒███ ▒███ ▒███
▒▒███     ███ ▒███      ▒███ ▒███  ▒███ ▒███  ▒███ ███▒███▒▒▒  ▒███ ▒███ ▒███ ▒███
 ▒▒█████████  █████     ▒▒███████  ▒███████   ▒▒█████ ▒▒██████ ▒▒████████▒▒██████ 
  ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒       ▒▒▒▒▒███  ▒███▒▒▒     ▒▒▒▒▒   ▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  
                         ███ ▒███  ▒███                                           
                        ▒▒██████   █████                                          
                         ▒▒▒▒▒▒   ▒▒▒▒▒                                           
</pre>

> Tool made by Edoardo

</div>

A terminal-based encryption/decryption tool supporting **Fernet** and **AES-256-GCM** encryption, with password-based or randomly generated keys.

---

## Features

- 🔐 **Fernet encryption** — simple, symmetric encryption with password or random key
- 🛡️ **AES-256-GCM encryption** — authenticated encryption, the same standard used by HTTPS
- 🔑 **Password-based keys** — derive a key from a memorable password using PBKDF2 + SHA256
- 🎲 **Random key generation** — generate a secure random key when you don't want a password
- 💥 **Graceful error handling** — wrong key? It won't crash, just tells you nicely

---

## Requirements

Python 3.x and the `cryptography` library:

```bash
pip install cryptography
```

---

## Usage

Run the script:

```bash
python network.py
```

You'll be greeted by the menu:

```
1. Simple fernet encryption
2. Simple fernet decryption
3. AES encryption
4. AES decryption
0. Quit program
```

### Fernet Encrypt / Decrypt
- Choose a **password** to derive a key, or leave blank to get a **random key**
- When using a random key, **save it** — without it you can't decrypt!
- When decrypting, choose whether you have a **password (p)** or a **raw key (k)**

### AES-256-GCM Encrypt / Decrypt
- Same password/key choice as Fernet
- Uses a random **IV (Initialization Vector)** prepended to the output automatically
- The encrypted output is **base64 encoded** so it's easy to copy and paste
- Authenticated encryption — if the message is tampered with, decryption will fail

---

## Security Notes

- Keys are derived using **PBKDF2HMAC with SHA-256** and 480,000 iterations
- AES uses **GCM mode** which provides both encryption and authentication
- The salt is currently fixed (`alligator2`) — for production use a random salt stored alongside the message
- IVs are always random (12 bytes) and stored with the ciphertext automatically

---

## To-Do

- [ ] Random salt per message (store alongside ciphertext for better security)
- [ ] Save encrypted output directly to a file
- [ ] Decrypt from a file
- [ ] Add a ChaCha20-Poly1305 encryption option
- [ ] Clipboard support — auto copy encrypted output instead of printing it

---

## License

Do whatever you want with it. Just don't encrypt anything illegal 😄
