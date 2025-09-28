namaBarang = input('Masukkan Nama Barang : ')
jumlahBarang = int(input('Masukkan Jumlah Barang : '))
hargaBarang = float(input('Masukkan Harga Barang : '))
member = int(input('Masukkan Kode Member (1=Platinum, 2=Gold, 3=Silver, 4=Non Member): '))

totalSebelumPPN = jumlahBarang * hargaBarang

if member == 1:
    diskonPersen = 25
elif member == 2:
    diskonPersen = 15
elif member == 3:
    diskonPersen = 5
elif member == 4:
    diskonPersen = 0
else:
    print("Kode member salah, Tidak ada diskon!!!")
    diskonPersen = 0

diskon = totalSebelumPPN * (diskonPersen / 100)
totalSetelahDiskon = totalSebelumPPN - diskon

totalSetelahPPN = totalSetelahDiskon + (totalSetelahDiskon * 0.12)

print("\n======= Struk Belanja =======")
print(f"Nama Barang              : {namaBarang}")
print(f"Jumlah Barang            : {jumlahBarang}")
print(f"Harga Barang             : Rp {hargaBarang}")
print(f"Total sebelum PPN        : Rp {totalSebelumPPN}")
print(f"Diskon {diskonPersen}%              : Rp {diskon}")
print(f"Total setelah Diskon     : Rp {totalSetelahDiskon}")
print(f"Total setelah PPN (12%)  : Rp {totalSetelahPPN}")
