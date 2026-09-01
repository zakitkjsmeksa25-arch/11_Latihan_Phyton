import math

# === FUNGSI MATEMATIKA & LOGIKA ===
def luas_segiempat(s):
    return s * s

def keliling_segiempat(s):
    return 4 * s

def apakah_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def cek_ganjil_genap(x):
    if x % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

def luas_bundaran(r):
    return 3.14 * r * r

def luas_tiga_sisi(a, t):
    return 0.5 * a * t


# === JALAN PROGRAM UTAMA ===
while True:
    print("\n=== UTILITY MATEMATIKA & LOGIKA ===")
    print("1. Hitung Luas Persegi")
    print("2. Hitung Keliling Persegi")
    print("3. Cek Bilangan Prima")
    print("4. Cek Bilangan Genap / Ganjil")
    print("5. Hitung Luas Lingkaran")
    print("6. Hitung Luas Segitiga")
    print("7. Keluar")
    print("===================================")
    
    pilihan = input("Pilih menu (1-7): ")
    
    if pilihan == "1":
        s = float(input("Masukkan sisi: "))
        print(f"Hasil Luas Persegi = {luas_segiempat(s)}")
        
    elif pilihan == "2":
        s = float(input("Masukkan sisi: "))
        print(f"Hasil Keliling Persegi = {keliling_segiempat(s)}")
        
    elif pilihan == "3":
        val = int(input("Masukkan angka: "))
        if apakah_prima(val):
            print(f"Angka {val} termasuk Bilangan Prima")
        else:
            print(f"Angka {val} Bukan Bilangan Prima")
            
    elif pilihan == "4":
        val = int(input("Masukkan angka: "))
        print(f"Angka {val} adalah Bilangan {cek_ganjil_genap(val)}")
            
    elif pilihan == "5":
        r = float(input("Masukkan jari-jari: "))
        print(f"Hasil Luas Lingkaran = {luas_bundaran(r)}")

    elif pilihan == "6":
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        print(f"Hasil Luas Segitiga = {luas_tiga_sisi(a, t)}")
        
    elif pilihan == "7":
        print("Selesai, terima kasih!")
        break
    else:
        print("Pilihan menu tidak ada, coba lagi!")
