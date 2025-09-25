#soal 3
nama = input("Masukkan nama barang : ")
harga = float(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah beli : "))

total_sebelum = harga * jumlah
pajak = total_sebelum * 0.12
total_bayar = total_sebelum + pajak

print("\nNama Barang       :", nama)
print("Harga Satuan      :", harga)
print("Jumlah            :", jumlah)
print("Total Sebelum Pajak:", total_sebelum)
print("Pajak (12%)       :", pajak)
print("Total Bayar       :", total_bayar)