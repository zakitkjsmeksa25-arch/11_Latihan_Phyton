def cek_ganjil_genap(x):
    while True:
      x = int(input("masukkan nilai: "))
    
      if x % 2 == 0:
         print("genap")
      else:
         print("ganjil")

if __name__ == "__main__":
    cek_ganjil_genap()