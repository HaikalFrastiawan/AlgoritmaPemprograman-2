# Input data
namaBarang = input('Masukkan Nama Barang : ')
jumlahBarang = int(input('Masukkan Jumlah Barang : '))
hargaBarang = float(input('Masukkan Harga Barang : '))

# Hitung total
totalSebelumPPN = jumlahBarang * hargaBarang
totalSetelahPPN = totalSebelumPPN * 1.12   # langsung tambah 12% PPN

# Cek diskon
if totalSetelahPPN >= 100000:
    totalAkhir = totalSetelahPPN * 0.9  # diskon 10%
else:
    totalAkhir = totalSetelahPPN

# Output struk
print("\n======= Struk Belanja =======")
print(f"Nama Barang              : {namaBarang}")
print(f"Jumlah Barang            : {jumlahBarang}")
print(f"Harga Barang             : Rp {hargaBarang}")
print(f"Total sebelum PPN        : Rp {totalSebelumPPN}")
print(f"Total setelah PPN        : Rp {totalSetelahPPN}")
print(f"Total setelah Diskon     : Rp {totalAkhir}")