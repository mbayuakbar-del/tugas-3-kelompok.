# =============================================================
# PROGRAM SISTEM MANAJEMEN NILAI MAHASISWA
# =============================================================

# Fungsi rekursif untuk menghitung total nilai
def rekursif_hitung_total(nilai, idx=0):
    if idx == len(nilai):
        return 0
    else:
        return nilai[idx] + rekursif_hitung_total(nilai, idx + 1)

# Menghitung rata-rata dari sebuah list nilai
def rata_rata(nilai):
    total = rekursif_hitung_total(nilai)  # pakai rekursi
    return total / len(nilai)


# =============================================================
# Menambahkan mahasiswa
def tambah_mahasiswa(data):
    nama = input("Masukkan nama mahasiswa: ")
    jumlah = int(input("Jumlah nilai yang ingin dimasukkan: "))

    nilai = []
    for i in range(jumlah):
        n = float(input(f"Nilai ke-{i+1}: "))
        nilai.append(n)

    data.append({"nama": nama, "nilai": nilai})
    print("Mahasiswa berhasil ditambahkan!\n")


# =============================================================
# Menampilkan laporan nilai
def tampilkan_laporan(data):
    print("\n===== LAPORAN NILAI MAHASISWA =====")
    for m in data:
        print(f"Nama : {m['nama']}")
        print(f"Nilai: {m['nilai']}")
        print(f"Rata-rata: {rata_rata(m['nilai']):.2f}")
        print("-------------------------------")
    print()


# =============================================================
# Cari mahasiswa berdasarkan nama
def cari_mahasiswa(nama_dicari, data):
    for m in data:
        if nama_dicari.lower() in m['nama'].lower():
            return m
    return None


# =============================================================
# Mendapatkan mahasiswa nilai tertinggi
def nilai_tertinggi(data):
    return max(data, key=lambda m: rata_rata(m["nilai"]))


# Mendapatkan mahasiswa nilai terendah
def nilai_terendah(data):
    return min(data, key=lambda m: rata_rata(m["nilai"]))


# =============================================================
# Menghitung rata-rata seluruh kelas
def rata_rata_kelas(data):
    if not data:
        return 0
    total = 0
    for m in data:
        total += rata_rata(m["nilai"])
    return total / len(data)


# =============================================================
# Program utama
def main():
    data_mahasiswa = []

    while True:
        print("\n===== SISTEM MANAJEMEN NILAI MAHASISWA =====")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Laporan Nilai")
        print("3. Cari Mahasiswa")
        print("4. Tampilkan Nilai Tertinggi & Terendah")
        print("5. Rata-rata Nilai Kelas")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_mahasiswa(data_mahasiswa)

        elif pilihan == "2":
            tampilkan_laporan(data_mahasiswa)

        elif pilihan == "3":
            nama = input("Masukkan nama yang dicari: ")
            hasil = cari_mahasiswa(nama, data_mahasiswa)
            if hasil:
                print("Data ditemukan:")
                print(hasil)
            else:
                print("Mahasiswa tidak ditemukan.\n")

        elif pilihan == "4":
            if data_mahasiswa:
                tinggi = nilai_tertinggi(data_mahasiswa)
                rendah = nilai_terendah(data_mahasiswa)
                print("\nMahasiswa dengan nilai tertinggi:")
                print(tinggi)
                print("\nMahasiswa dengan nilai terendah:")
                print(rendah)
            else:
                print("Data kosong!\n")

        elif pilihan == "5":
            print(f"Rata-rata nilai kelas: {rata_rata_kelas(data_mahasiswa):.2f}\n")

        elif pilihan == "6":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid!\n")


# Menjalankan program utama
main()
