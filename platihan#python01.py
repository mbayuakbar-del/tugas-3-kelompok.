antrian = ["budi","sari","dian","eko"] 
antrian.append("rara")
antrian.insert(2,"bayu")
#akses satu elemen berdasarakan indeks
print("pelanggan pertama :", antrian [0]) 
#indeks 0 = depan
print ("pelanggan terakhir :", antrian [-1])
#indeks -1 = belakang
print ("pelanggan ke-3 :", [2])
#indeks 2 # akses panjang antrian 
print("jumlah antrian :",len(antrian))
print("\n Daftar antrian :")
for i , nama in enumerate(antrian):
    print (f"[{i}] {nama}")
print("\n Apakah sari ada di antrian?","sari" in antrian)  
print("apakah tono ada di antrian?","tono" in antrian) 
print ( antrian [ 1:] )
print(antrian[0:])
print ( antrian [1:2] )
print("antrian")