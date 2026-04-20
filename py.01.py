print(input("masukan nama kamu: "))
print(input("masukan prodimu TI/TI: "))
print(input("masukan nim: "))

print("=== OPERATOR PERBANDINGAN ===")

a=int(input("masukan angka pertama:"))
b=int(input("masukan angka kedua:"))

print("\n=====hasil bilangan yang paling besar===")

if a>b:
    print(f"bilangan terbesar adalah :{a}")
elif b>a:
    print(f"bilangan terbesar adalah :{b}")
else:
    print(f"kedua bilangan sama besar(nilai{a})")

print("kamu berhasil menghitung nilai yang lebih besar dari bilangan lainnya")    
