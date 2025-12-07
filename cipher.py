# cipher.py

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def encrypt(text, key):
    res = ""
    for ch in text.lower():
        if ch in ALPHABET:
            res += ALPHABET[(ALPHABET.index(ch) + key) % 26]
        else:
            res += ch
    return res

def decrypt(text, key):
    return encrypt(text, -key)