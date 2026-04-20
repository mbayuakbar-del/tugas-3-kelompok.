"""
PROGRAM SISTEM RESTORAN
Menggunakan Queue + Stack
"""

# =========================================
# BAGIAN 1 — STRUKTUR DATA
# =========================================

class StrukturData:
    def __init__(self):
        self.data = []

    def tambah_belakang(self, item):  # enqueue
        self.data.append(item)

    def tambah_depan(self, item):  # prioritas (VIP)
        self.data.insert(0, item)

    def ambil_depan(self):  # dequeue
        if not self.kosong():
            return self.data.pop(0)
        return None

    def lihat(self):
        return self.data

    def kosong(self):
        return len(self.data) == 0


# =========================================
# BAGIAN 2 — SISTEM RESTORAN
# =========================================

class SistemRestoran:
    def __init__(self):
        self.antrian = StrukturData()
        self.riwayat = []  # stack untuk undo

    def tambah_pelanggan(self, nama, tipe):
        pelanggan = {"nama": nama, "tipe": tipe}

        if tipe.lower() == "vip":
            self.antrian.tambah_depan(pelanggan)
            print(f"{nama} (VIP) masuk ke depan antrian")
        else:
            self.antrian.tambah_belakang(pelanggan)
            print(f"{nama} masuk ke antrian")

        self.riwayat.append(pelanggan)  # simpan ke stack

    def batalkan_pesanan(self):
        if len(self.riwayat) == 0:
            print("Tidak ada pesanan untuk dibatalkan")
            return

        terakhir = self.riwayat.pop()

        if terakhir in self.antrian.data:
            self.antrian.data.remove(terakhir)
            print(f"Pesanan {terakhir['nama']} dibatalkan")
        else:
            print("Pesanan sudah diproses, tidak bisa dibatalkan")

    def proses_dapur(self):
        if self.antrian.kosong():
            print("Tidak ada pesanan")
            return

        pelanggan = self.antrian.ambil_depan()
        print(f"Memproses pesanan: {pelanggan['nama']} ({pelanggan['tipe']})")

    def tampilkan_antrian(self):
        if self.antrian.kosong():
            print("Antrian kosong")
            return

        print("\n=== DAFTAR ANTRIAN ===")
        for i, p in enumerate(self.antrian.lihat(), start=1):
            print(f"{i}. {p['nama']} ({p['tipe']})")


# =========================================
# BAGIAN 3 — MENU
# =========================================

def menu():
    sistem = SistemRestoran()

    while True:
        print("\n=== SISTEM RESTORAN ===")
        print("1. Tambah Pelanggan")
        print("2. Proses Pesanan")
        print("3. Batalkan Pesanan (Undo)")
        print("4. Lihat Antrian")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Nama pelanggan: ")
            tipe = input("Tipe (normal/vip): ")
            sistem.tambah_pelanggan(nama, tipe)

        elif pilihan == "2":
            sistem.proses_dapur()

        elif pilihan == "3":
            sistem.batalkan_pesanan()

        elif pilihan == "4":
            sistem.tampilkan_antrian()

        elif pilihan == "0":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")


# =========================================
# ENTRY POINT
# =========================================

if __name__ == "__main__":
 
  menu()     