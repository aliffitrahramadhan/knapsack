# knapsack.py
# Modul berisi fungsi untuk generate_key, encrypt, dan decrypt
# Implementasi algoritma Merkle–Hellman Knapsack

from math import gcd

def generate_key():
    """Membangkitkan kunci publik dan privat untuk algoritma Knapsack"""
    # Deret super-increasing sebagai kunci privat
    w = [2, 3, 7, 14, 30, 57, 120, 251]
    # Modulus dan multiplier
    m = 500
    n = 41
    # Pastikan gcd(n, m) = 1
    if gcd(n, m) != 1:
        raise ValueError("n dan m tidak relatif prima!")
    # Hitung kunci publik
    b = [(n * wi) % m for wi in w]
    return w, b, n, m


def encrypt(plaintext, public_key):
    """Melakukan proses enkripsi pesan teks menjadi ciphertext"""
    b = public_key
    bits = ''.join(format(ord(c), '08b') for c in plaintext)  # konversi teks ke biner
    ciphertext = []
    for i in range(0, len(bits), len(b)):
        block = bits[i:i+len(b)]
        C = sum(int(bit) * b[j] for j, bit in enumerate(block))
        ciphertext.append(C)
    return ciphertext


def mod_inverse(n, m):
    """Mencari invers n terhadap m"""
    for i in range(1, m):
        if (n * i) % m == 1:
            return i
    return None


def decrypt(ciphertext, private_key, n, m):
    """Melakukan proses dekripsi ciphertext menjadi plaintext"""
    w = private_key
    n_inv = mod_inverse(n, m)
    if n_inv is None:
        raise ValueError("Invers modular tidak ditemukan!")

    bits = ''
    for C in ciphertext:
        C_ = (C * n_inv) % m
        temp = []
        for wi in reversed(w):
            if wi <= C_:
                temp.append('1')
                C_ -= wi
            else:
                temp.append('0')
        temp.reverse()
        bits += ''.join(temp)

    plaintext = ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))
    return plaintext