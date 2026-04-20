print(input("masukan nama : "))
print(input("masukan prodi : "))
print(input("masukan NIM : "))

print("===operator perbandingan===")
usia=int(input("masukkan usia anda:"))

if usia < 12:
    kategori=("anak-anak")
elif usia == 12-17:
    kategori=("remaja")
elif usia == 18-59:
    kategori=("dewasa")


print("selamat anda sudah bisa meng kategorikan umur",kategori)    
