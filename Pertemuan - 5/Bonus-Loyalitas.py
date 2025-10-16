# Program Bonus Loyalitas (Tanpa Pruning)
print("\n=== Program Bonus Loyalitas (Tanpa Pruning) ===")

masa_kerja = int(input("Masukkan Masa Kerja (tahun): "))
sertifikasi = input("Apakah memiliki sertifikasi profesional relevan? (ya/tidak): ").lower()

print(f"\nCek 1: Masa kerja > 5 tahun -> {masa_kerja > 5}")
print(f"Cek 2: Sertifikasi relevan -> {sertifikasi == 'ya'}")

if masa_kerja > 5:
    if sertifikasi == "ya":
        print(" Karyawan MENDAPAT Bonus Loyalitas (Masa kerja & sertifikasi)")
    else:
        print(" Karyawan MENDAPAT Bonus Loyalitas (Masa kerja saja)")
else:
    if sertifikasi == "ya":
        print(" Karyawan MENDAPAT Bonus Loyalitas (Sertifikasi saja)")
    else:
        print(" Karyawan TIDAK mendapat Bonus Loyalitas")


# Program Bonus Loyalitas (Dengan Pruning)
print("\n=== Program Bonus Loyalitas (Dengan Pruning) ===")

masa_kerja = int(input("Masukkan Masa Kerja (tahun): "))
sertifikasi = input("Apakah memiliki sertifikasi profesional relevan? (ya/tidak): ").lower()

if masa_kerja > 5:
    print(" Masa kerja memenuhi syarat (>5 tahun)")
    print(" Karyawan MENDAPAT Bonus Loyalitas")
else:
    print(" Masa kerja kurang dari 5 tahun")
    if sertifikasi == "ya":
        print(" Namun memiliki sertifikasi relevan")
        print(" Karyawan MENDAPAT Bonus Loyalitas")
    else:
        print(" Tidak memiliki sertifikasi relevan")
        print(" Karyawan TIDAK mendapat Bonus Loyalitas")