# attack.py

from cipher import decrypt, ALPHABET
from collections import Counter

# English letter probability (%) (normalized)
ENGLISH_FREQ = {
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 
    'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025,
    'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987,
    's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150,
    'y': 1.974, 'z': 0.074
}


def chi_square_score(text):
    """Return chi-square score comparing text frequency to English"""
    text = ''.join(ch for ch in text.lower() if ch in ALPHABET)
    if not text:
        return float('inf')

    text_len = len(text)
    freq = Counter(text)

    chi = 0
    for ch in ALPHABET:
        observed = freq.get(ch, 0)
        expected = ENGLISH_FREQ[ch] * text_len / 100
        chi += (observed - expected) ** 2 / (expected + 1e-9)  # avoid division by zero
    return chi


def crack(cipher_text):
    """Try all 26 keys and choose best (lowest chi-square score)"""
    best_key = None
    best_plain = ""
    best_score = float('inf')

    for key in range(26):
        candidate = decrypt(cipher_text, key)
        score = chi_square_score(candidate)

        if score < best_score:
            best_score = score
            best_key = key
            best_plain = candidate

    return best_key, best_plain
