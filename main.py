# main.py
from cipher import encrypt, decrypt
from attack import crack

if __name__ == "__main__":
    text = "security is fun and cryptography is art"
    key = 7

    print("Original:", text)
    enc = encrypt(text, key)
    print("Encrypted:", enc)

    guessed_key, plaintext = crack(enc)
    print("\n🔐 Auto-Crack Results")
    print("Guessed Key:", guessed_key)
    print("Decrypted:", plaintext)