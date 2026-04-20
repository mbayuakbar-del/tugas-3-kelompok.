#NAMA : M.BAYU AKBAR
#NIM  : TI22250020

print("==========SISTEM INPUT NILAI MAHASISWA==========")

daftar = ["TATA", "IRFAN", "BAYU", "DENY", "NABIL"]
# FOR LOOP
print("\nMahasiswa terdaftar:")
no = 1
for d in daftar:
    print(no, d)
    no += 1

# Hitung nama vokal
vokal = "AIUEOaiueo"
jv = 0
for d in daftar:
    if d[0] in vokal:
        jv += 1

print("Jumlah nama vokal:", jv)

# WHILE LOOP untuk MENU
menu = ""
extra = []

while menu != "5":
    print("\n=== MENU UTAMA ===")
    print("1. Lihat daftar mahasiswa")
    print("2. Cari data mahasiswa")
    print("3. Tambah mahasiswa baru")
    print("4. Pola segitiga nama mahasiswa")
    print("5. Keluar program")

    menu = input("Pilih opsi: ")

    if menu == "1":
        print("\nLIST:")
        no = 1
        for x in daftar + extra:
            print(no, x)
            no += 1

    elif menu == "2":
        cari = input("Cari nama: ")
        ketemu = False

        for x in daftar + extra:
            if x == cari:
                print("Ditemukan:", x)
                ketemu = True
                break

        if ketemu == False:
            print("Nama tidak ada!")

    elif menu == "3":
        baru = input("Tambah nama: ")
        extra.append(baru)
        print("Nama ditambahkan!")

    elif menu == "4":
        print("\nPOLA SEGITIGA SEMUA NAMA:")
        for nama in daftar + extra:
            temp = ""
            for h in nama:
                temp += h
                print(temp)
            print()

    elif menu == "5":
        print("Program ditutup...")

    else:
        print("Pilihan salah!")

# DO WHILE
print("\nINPUT NILAI MAHASISWA (3 ORANG)")

nilai = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

mk = ["MTK","FISIKA","KIMIA"]

i = 0
while i < 3:
    print("\nInput nilai:", daftar[i])
    j = 0
    while j < 3:
        while True:
            n = int(input("  Nilai " + mk[j] + ": "))
            if 0 <= n <= 100:
                break
            print("  Nilai harus 0-100!")

        nilai[i][j] = n
        j += 1

    i += 1

# NESTED LOOP
print("\nTABEL NILAI:")
print("----------------------------------------------")
print("Nama  |  MTK | FISIKA | KIMIA | Rata-rata")
print("----------------------------------------------")

i = 0
while i < 3:
    tot = nilai[i][0] + nilai[i][1] + nilai[i][2]
    rt = int((tot/3)*100)/100

    print(
        daftar[i], " | ",
        nilai[i][0], " | ",
        nilai[i][1], "   | ",
        nilai[i][2], "  | ",
        rt
    )
    i += 1

print("----------------------------------------------")

# CONTINUE
print("\nRata-rata >= 80:")
i = 0
while i < 3:
    r = (nilai[i][0] + nilai[i][1] + nilai[i][2]) / 3

    if r < 80:
        i += 1
        continue

    print(daftar[i], "-", r)
    i += 1
