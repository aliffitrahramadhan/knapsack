# 🧩 Merkle–Hellman Knapsack Cryptography

Implementasi algoritma **Merkle–Hellman Knapsack** menggunakan **Python** untuk proses **enkripsi dan dekripsi pesan teks digital**.
Proyek ini merupakan bagian dari Tugas Besar Kriptografi – **Universitas Dipa Makassar** (2025).

---

## 📂 Struktur Folder Proyek

```

Struktur folder sesuai implementasi pada Visual Studio Code:
KNAPSACK

│

├── _pycache_/               # Cache otomatis Python

├── knapsack.py                # Modul: generate_key(), encrypt(), decrypt()

├── main.py                    # Program utama untuk menjalankan proses

├── plaintext.txt              # File input pesan asli

└── ciphertext.txt             # File hasil enkripsi

```
## ⚙ Cara Menjalankan Program
1️⃣ Persiapan

Pastikan Python 3.x sudah terpasang pada perangkat Anda.

Opsional: install module tambahan bila diperlukan

pip install -r requirements.txt

```
```
## 2️⃣ Menjalankan program

Buka terminal pada folder proyek:

python main.py

```
```
### Program akan:

Membaca plaintext.txt

Melakukan enkripsi menggunakan algoritma Merkle–Hellman Knapsack

Menyimpan hasil ke ciphertext.txt

Melakukan dekripsi kembali

Menampilkan hasil di terminal

Menyimpan hasil dekripsi ke decrypted_output.txt
```
```
## 🧠 Ringkasan Algoritma

Merkle–Hellman Knapsack merupakan algoritma kriptografi kunci publik yang bekerja berdasarkan super-increasing knapsack dan subset sum problem.
```
```
### Tahapan Utama
🔹 Key Generation

Tentukan deret super-increasing w

Pilih modulus m dan multiplier n dengan syarat gcd(n, m) = 1

Hitung kunci publik

𝑏
𝑖
=
(
𝑛
⋅
𝑤
𝑖
)
m
o
d
 
 
𝑚
b
i
	​

=(n⋅w
i
	​

)modm
```
```
### 🔹Encrypt

Konversi pesan → biner ASCII

Ciphertext dihitung dengan:

𝐶
=
∑
𝑖
=
1
𝑛
𝛼
𝑖
𝑏
𝑖
C=
i=1
∑
n
	​

α
i
	​

b
i
```	​
```
### 🔹 Decrypt

Hitung invers modular:

𝑛
−
1
m
o
d
 
 
𝑚
n
−1
modm

Kembalikan ciphertext → plaintext menggunakan teknik greedy pada deret privat w.
```
```
## 🧪 Contoh Hasil Eksekusi

Output terminal:

=== HASIL PROSES KNAPSACK ===
Pesan Asli       : HELLO WORLD
Ciphertext       : [681, 945, 732, 580, 810, 913, 701, 621, 750, 830, 540, 967]
Hasil Dekripsi   : HELLO WORLD
```
```
### Isi file:
```
```
### plaintext.txt

HELLO WORLD
```
```
### ciphertext.txt

681 945 732 580 810 913 701 621 750 830 540 967
```
```
### decrypted_output.txt

HELLO WORLD
```
```
## 📸 Screenshot Antarmuka VS Code

Struktur folder & hasil terminal ditampilkan pada makalah (Lampiran).
Disertakan untuk menunjukkan eksekusi program secara langsung.

### 🔗 Pranala Penting
📁 Repository GitHub

➡ https://github.com/aliffitrahramadhan/knapsack

### 🎥 Video Demo Program

➡ (Tambahkan tautan YouTube / Google Drive di sini)

### 👨‍💻 Penulis

Alif Fitrah Ramadhan
Program Studi Teknik Informatika
Universitas Dipa Makassar
2025

### 📝 Lisensi

Proyek ini dibuat untuk keperluan akademik dan pembelajaran konsep kriptografi.
Tidak direkomendasikan untuk digunakan sebagai sistem keamanan produksi.
