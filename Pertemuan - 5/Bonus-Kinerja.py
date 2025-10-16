# Program Bonus Kinerja (Tanpa Pruning)
print("=== Program Bonus Kinerja (Tanpa Pruning) ===")

# Input
penilaian = float(input("Masukkan Penilaian Kinerja (1-10): "))
kehadiran = float(input("Masukkan Persentase Kehadiran: "))

print(f"\nCek 1: Apakah penilaian > 8? -> {penilaian > 8}")
print(f"Cek 2: Apakah kehadiran > 95%? -> {kehadiran > 95}")

# Logika tanpa pruning (semua kondisi dicek terpisah)
if penilaian > 8:
    if kehadiran > 95:
        print(" Karyawan MENDAPAT Bonus Kinerja")
    else:
        print(" Karyawan TIDAK mendapat Bonus Kinerja (Kehadiran kurang)")
else:
    if kehadiran > 95:
        print(" Karyawan TIDAK mendapat Bonus Kinerja (Nilai rendah)")
    else:
        print(" Karyawan TIDAK mendapat Bonus Kinerja (Nilai & Kehadiran rendah)")


# Program Bonus Kinerja (Dengan Pruning)
print("=== Program Bonus Kinerja (Dengan Pruning) ===")

penilaian = float(input("Masukkan Penilaian Kinerja (1-10): "))
kehadiran = float(input("Masukkan Persentase Kehadiran: "))

if penilaian > 8:
    print(" Penilaian memenuhi syarat ( >8)")
    if kehadiran > 95:
        print(" Kehadiran memenuhi syarat (>95%)")
        print(" Karyawan MENDAPAT Bonus Kinerja")
    else:
        print(" Kehadiran tidak memenuhi syarat")
        print(" Tidak mendapat Bonus Kinerja")
else:
    print(" Penilaian tidak memenuhi syarat")
    print(" Tidak mendapat Bonus Kinerja")