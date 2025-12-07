# attack.py

from collections import Counter
from cipher import decrypt, ALPHABET

# English letter frequency (approx)
COMMON = "etaoinshrdlcumwfgypbvkjxqz"

def crack(cipher_text):
    # Count frequency in text
    freq = Counter(ch for ch in cipher_text.lower() if ch in ALPHABET)
    if not freq:
        return None, ""

    # Most frequent character in the text
    most_common_in_text = freq.most_common(1)[0][0]

    # Assume frequent char corresponds to 'e'
    assumed_key = (ALPHABET.index(most_common_in_text) - ALPHABET.index("e")) % 26

    return assumed_key, decrypt(cipher_text, assumed_key)