while True:
    print("\n===== MENU UTAMA =====")
    print("1. Modul Matematika")
    print("2. Modul Bangun Ruang")
    print("3. Keluar")
    print("======================")

    pilihan = input("Pilih menu : ")

    # MODUL MATEMATIKA
    if pilihan == "1":
        while True:
            print("\n===== MODUL MATEMATIKA =====")
            print("1. Cek Bilangan Ganjil/Genap")
            print("2. Cek Bilangan Prima")
            print("3. Kalkulator")
            print("4. Keluar")
            print("============================")

            menu = input("Pilih menu : ")

            if menu == "1":
                x = int(input("Masukkan angka : "))

                if x % 2 == 0:
                    print("Bilangan genap")
                else:
                    print("Bilangan ganjil")

            elif menu == "2":
                x = int(input("Masukkan angka : "))

                if x < 2:
                    print("Bukan bilangan prima")
                else:
                    prima = True

                    for i in range(2, x):
                        if x % i == 0:
                            prima = False
                            break

                    if prima:
                        print("Bilangan prima")
                    else:
                        print("Bukan bilangan prima")

            elif menu == "3":
                print("\n===== KALKULATOR =====")
                angka1 = float(input("Masukkan angka pertama : "))
                operator = input("Masukkan operator (+, -, *, /) : ")
                angka2 = float(input("Masukkan angka kedua : "))

                if operator == "+":
                    print("Hasil =", angka1 + angka2)
                elif operator == "-":
                    print("Hasil =", angka1 - angka2)
                elif operator == "*":
                    print("Hasil =", angka1 * angka2)
                elif operator == "/":
                    if angka2 != 0:
                        print("Hasil =", angka1 / angka2)
                    else:
                        print("Tidak bisa dibagi 0")
                else:
                    print("Operator tidak tersedia")

            elif menu == "4":
                print("Kembali ke menu utama.")
                break

            else:
                print("Pilihan tidak tersedia.")

    # MODUL BANGUN RUANG
    elif pilihan == "2":
        while True:
            print("\n===== MODUL BANGUN RUANG =====")
            print("1. Luas Persegi Panjang")
            print("2. Luas Segitiga")
            print("3. Luas Persegi")
            print("4. Luas Lingkaran")
            print("5. Keluar")
            print("==============================")

            menu = input("Pilih menu : ")

            if menu == "1":
                panjang = float(input("Masukkan panjang : "))
                lebar = float(input("Masukkan lebar : "))

                luas = panjang * lebar
                print("Luas persegi panjang =", luas)

            elif menu == "2":
                alas = float(input("Masukkan alas : "))
                tinggi = float(input("Masukkan tinggi : "))

                luas = 0.5 * alas * tinggi
                print("Luas segitiga =", luas)

            elif menu == "3":
                sisi = float(input("Masukkan sisi : "))

                luas = sisi * sisi
                print("Luas persegi =", luas)

            elif menu == "4":
                jari = float(input("Masukkan jari-jari : "))

                luas = 3.14 * jari * jari
                print("Luas lingkaran =", luas)

            elif menu == "5":
                print("Kembali ke menu utama.")
                break

            else:
                print("Pilihan tidak tersedia.")

    # KELUAR
    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")

    print("---------------------------")