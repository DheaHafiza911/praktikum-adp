import json

DATA_FILE = "data_keuangan.txt"


def baca_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def simpan_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def tampilkan_data(data):
    print("\n=== Daftar Keuangan ===")
    if not data:
        print("Belum ada data tersimpan.\n")
        return
    for tanggal, transaksi in data.items():
        print(f"Tanggal: {tanggal}")
        for item in transaksi:
            print(f"  Keterangan: {item['keterangan']}")
            print(f"  Jumlah: {item['jumlah']} | Tipe: {item['tipe']}")
        print("-" * 30)


def tambah_data(data):
    tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
    keterangan = input("Masukkan keterangan: ")
    jumlah = int(input("Masukkan jumlah uang: "))
    tipe = input("Tipe (pemasukan/pengeluaran): ").lower()

    if tanggal not in data:
        data[tanggal] = []
    
    data[tanggal].append({"keterangan": keterangan, "jumlah": jumlah, "tipe": tipe})
    simpan_data(data)
    print("Data berhasil ditambahkan!")

def hapus_data(data):
    tanggal = input("Masukkan tanggal data yang ingin dihapus: ")
    if tanggal in data:
        del data[tanggal]
        simpan_data(data)
        print("Data berhasil dihapus!")
    else:
        print("Data tidak ditemukan.")

def main():
    data = baca_data()

    while True:
        print("\n=== Menu Keuangan ===")
        print("1. Tambah Data Keuangan")
        print("2. Hapus Data Keuangan")
        print("3. Tampilkan Semua Data")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_data(data)
        elif pilihan == "2":
            hapus_data(data)
        elif pilihan == "3":
            tampilkan_data(data)
        elif pilihan == "4":
            print("Terima kasih telah menggunakan pencatatan keuangan!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def jalankan_program():
    main()

jalankan_program()
