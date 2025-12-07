# attack.py

from cipher import decrypt, ALPHABET
from collections import Counter

# English letter frequency ranking (approx)
COMMON = "etaoinshrdlcumwfgypbvkjxqz"


def score_english(text):
    """Score text by counting common letters; higher = more likely correct."""
    return sum(text.count(ch) for ch in COMMON[:6])  # e,t,a,o,i,n


def crack(cipher_text):
    """Try all 26 keys and pick the best score."""
    best_key = None
    best_score = -1
    best_plain = ""

    for key in range(26):
        candidate = decrypt(cipher_text, key)
        score = score_english(candidate.lower())

        if score > best_score:
            best_score = score
            best_key = key
            best_plain = candidate

    return best_key, best_plain
