# main.py
# Program utama untuk menjalankan proses enkripsi dan dekripsi

from knapsack import generate_key, encrypt, decrypt

# Baca pesan asli dari file plaintext.txt
with open("plaintext.txt", "r") as file:
    plaintext = file.read().strip()

# Bangkitkan kunci
w, b, n, m = generate_key()

# Enkripsi pesan
ciphertext = encrypt(plaintext, b)
with open("ciphertext.txt", "w") as file:
    file.write(' '.join(map(str, ciphertext)))

# Dekripsi pesan kembali
with open("ciphertext.txt", "r") as file:
    cipher_data = list(map(int, file.read().split()))

decrypted = decrypt(cipher_data, w, n, m)

print("=== HASIL PROSES KNAPSACK ===")
print("Pesan Asli       :", plaintext)
print("Ciphertext       :", cipher_data)
print("Hasil Dekripsi   :", decrypted)

# Simpan hasil dekripsi untuk verifikasi tambahan
with open("decrypted_output.txt", "w") as file:
    file.write(decrypted)