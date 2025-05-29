def input_praktikan():
    praktikan = []
    n = int(input("Masukkan jumlah praktikan: "))
    for i in range(n):
        print(f"\nMasukkan data praktikan {i+1}:")
        nama = input("Nama: ")
        nim = input("NIM: ")
        pretest = float(input("Nilai Pretest: "))
        postest = float(input("Nilai Postest: "))
        tugas = float(input("Nilai Tugas/Makalah: "))
        bonus = float(input("Nilai Bonus: "))
        nilai_akhir = (0.25 * pretest) + (0.25 * postest) + (0.5 * tugas) + bonus
        praktikan.append({"Nama": nama, "NIM": nim, "Nilai Akhir": nilai_akhir})
    return praktikan


def hitung_rata_rata(praktikan):
    
    total = 0
    for p in praktikan:
        total += p["Nilai Akhir"]
    return total / len(praktikan)

def urutkan_praktikan(praktikan):
    n = len(praktikan)
    for i in range(n):
        for j in range(i + 1, n):
            if praktikan[i]["Nilai Akhir"] < praktikan[j]["Nilai Akhir"]:
                praktikan[i], praktikan[j] = praktikan[j], praktikan[i]  

    peringkat = 1
    for p in praktikan:
        p["Peringkat"] = peringkat
        peringkat += 1
    return praktikan

praktikan = input_praktikan()
rata_rata = hitung_rata_rata(praktikan)
praktikan_sorted = urutkan_praktikan(praktikan)

print("\nTABEL HASIL PENILAIAN PRAKTIKAN")
print("=" * 48)
print("Nama           NIM         Nilai Akhir  Peringkat")
print("=" * 48)
for p in praktikan_sorted:
    print(f"{p['Nama']:15} {p['NIM']:10} {p['Nilai Akhir']:12.2f} {p['Peringkat']:8}")
print("=" * 48)
print(f"\nRata-rata Nilai Akhir: {rata_rata:.2f}")

