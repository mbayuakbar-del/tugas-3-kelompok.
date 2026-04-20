# ============================================
#   SISTEM NILAI MAHASISWA - Menggunakan List
# ============================================

daftar_nilai = []   # List untuk menyimpan nilai
# --- Fungsi 1: Tambah nilai ke dalam list ---
def tambah_nilai(nilai):
    # TODO: tambahkan 'nilai' ke dalam daftar_nilai
    daftar_nilai.append()
# --- Fungsi 2: Hitung rata-rata ---
def hitung_rata_rata():
    if len(daftar_nilai) == 0:
        return 0
    # TODO: hitung dan kembalikan nilai rata-rata
    return sum(daftar_nilai)
# --- Fungsi 3: Cari nilai tertinggi ---
def cari_tertinggi():
    # TODO: kembalikan nilai tertinggi dari daftar_nilai
    return max(daftar_nilai)
daftar_nilai 
# --- Fungsi 4: Cari nilai terendah ---
def cari_terendah():
    # TODO: kembalikan nilai terendah dari daftar_nilai
    return min(daftar_nilai)
daftar_nilai 
# --- Fungsi 5: Tampilkan semua nilai ---
def tampilkan_nilai():
    print("\n=== Daftar Nilai Mahasiswa ===")
    # TODO: tampilkan semua nilai dengan nomor urut
    #       contoh output:
    #       1. 85
    #       2. 90
    #       3. 78
    pass
# ============================================
#   PROGRAM UTAMA (jangan diubah)
# ============================================
print("=== Input Nilai Mahasiswa ===")
n = int(input("Masukkan jumlah mahasiswa: "))

for i in range(n):
    nilai = float(input(f"Nilai mahasiswa ke-{i+1}: "))
    tambah_nilai(nilai)

tampilkan_nilai()

print(f"\nRata-rata nilai   : {hitung_rata_rata():.2f}")
print(f"Nilai tertinggi   : {cari_tertinggi()}")
print(f"Nilai terendah    : {cari_terendah()}")