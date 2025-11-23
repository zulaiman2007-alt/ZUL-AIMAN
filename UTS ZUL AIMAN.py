# Program penentuan nilai tempat

# Daftar nama nilai tempat
nilai_tempat = {
    1: "satuan",
    2: "puluhan",
    3: "ratusan",
    4: "ribuan",
    5: "puluh ribuan",
    6: "ratus ribuan",
    7: "jutaan",
    8: "puluh jutaan",
    9: "ratus jutaan"
}

print("=== Program Nilai Tempat Bilangan ===")
bil = input("Masukkan sebuah bilangan: ")

print("\nHasil analisis nilai tempat:")
print("-------------------------------------")

# Hitung jumlah digit
jumlah_digit = len(bil)

# Proses setiap digit
for indeks, karakter in enumerate(bil):
    
    # Posisi dari belakang
    urutan = jumlah_digit - indeks
    
    # Ambil nama nilai tempat
    nama_tempat = nilai_tempat.get(urutan, "nilai tempat tidak diketahui")
    
    print(f"Digit '{karakter}' berada pada posisi {nama_tempat}")
