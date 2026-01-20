import math

def hitung(pilih):
    if pilih == "1":
        s = float(input("Masukkan sisi: "))
        luas = s * s
        keliling = 4 * s

    elif pilih == "2":
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        luas = p * l
        keliling = 2 * (p + l)

    elif pilih == "3":
        r = float(input("Masukkan jari-jari: "))
        luas = math.pi * r * r
        keliling = 2 * math.pi * r

    elif pilih == "4":
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        sisi_miring = (a**2 + t**2) ** 0.5
        luas = 0.5 * a * t
        keliling = a + t + sisi_miring

    else:
        return None, None

    return luas, keliling


def main():
    print("=" * 30)
    print("   APLIKASI BANGUN DATAR")
    print("=" * 30)

    nama = input("Masukkan nama Anda: ")

    while True:
        print("\nMenu Bangun Datar:")
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Lingkaran")
        print("4. Segitiga Siku-siku")

        pilih = input("Pilih (1-4): ")

        luas, keliling = hitung(pilih)

        if luas is None:
            print("❌ Pilihan tidak valid!")
            continue

        print(f"\nLuas     : {luas:.2f}")
        print(f"Keliling: {keliling:.2f}")

        ulang = input("\nHitung lagi? (y/n): ").lower()
        if ulang != "y":
            print(f"\nTerima kasih, {nama} 🙏")
            break


if __name__ == "__main__":
    main()