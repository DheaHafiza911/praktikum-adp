# List untuk menyimpan data mahasiswa
data_mahasiswa = []

while True:
    print("Menu:")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Keluar")
    pilihan = input("Pilih opsi: ")

    if pilihan == "1":
        nomor = (input("Masukkan NIM mahasiswa: "))
        nama = (input("Masukkan nama mahasiswa: "))
        nilai = float(input("Masukkan nilai mahasiswa: "))
        data_mahasiswa.append((nomor, nama, nilai))
        print("Data berhasil ditambahkan!\n")

    elif pilihan == "2":
        nomor = input("Masukkan nomor mahasiswa yang ingin dihapus: ")
        data_mahasiswa = [mhs for mhs in data_mahasiswa if mhs[0] != nomor]
        print("Data berhasil dihapus!\n")

    elif pilihan == "3":
        if not data_mahasiswa:
            print("Tidak ada data mahasiswa.\n")
        else:
            # Mengurutkan data berdasarkan nilai dari tertinggi ke terendah dengan Bubble Sort
            for i in range(len(data_mahasiswa) - 1):
                for j in range(i + 1, len(data_mahasiswa)):
                    if data_mahasiswa[i][2] < data_mahasiswa[j][2]:
                        data_mahasiswa[i], data_mahasiswa[j] = data_mahasiswa[j], data_mahasiswa[i]

            # Menampilkan data mahasiswa yang telah diurutkan
            print("\nData Mahasiswa:")
            print("{:<15} {:<20} {:<10}".format("nomor", "Nama", "Nilai"))
            print("="*45)
            for nomor, nama, nilai in data_mahasiswa:
                print("{:<15} {:<20} {:<10}".format(nomor, nama, nilai))
            print("\n")

    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini!")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.\n")
