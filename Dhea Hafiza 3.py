#Ukuran kursi
baris = 6
kolom = 5

# Inisialisasi kursi
kursi = [str(i + 1) for i in range(baris * kolom)]

# Harga tiket berdasarkan kategori
harga_tiket = {
    "VVIP": 2000000,
    "VIP": 1500000,
    "Reguler": 1000000,
    "Ekonomi": 500000
}

# Kategori kursi
kategori_kursi = {
    "VVIP": kursi[:10],  # Kursi 1-10
    "VIP": kursi[10:15],  # Kursi 11-15
    "Reguler": kursi[15:25],  # Kursi 16-25
    "Ekonomi": kursi[25:]  # Kursi 26-30
}

# Selamat datang
print("Selamat datang di sistem reservasi tiket konser!\n")

# Tampilkan layout kursi
print("Tampilan Layout Kursi:")
for i in range(baris):
    print(" ".join(kursi[i * kolom:(i + 1) * kolom]))
print()

# Tampilkan harga tiket
print("Harga Tiket")
for kategori, harga in harga_tiket.items():
    print(f"{kategori}: Rp{harga:,}")
print()

# Mulai proses pemesanan
jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dipesan: "))

for i in range(jumlah_tiket):
    print(f"Pemesanan ke-{i + 1}:")
    nama = input("Masukkan nama Anda: ")
    no_kursi = input("Masukkan nomor kursi yang ingin dipesan: ")
    
    if no_kursi in kursi:
        password = input("Buat password untuk akses konser: ")
        
        # Tentukan kategori berdasarkan nomor kursi
        for k, daftar_kursi in kategori_kursi.items():
            if no_kursi in daftar_kursi:
                kategori = k
                break
        
        # Harga tiket
        harga = harga_tiket[kategori]
        
        # Hapus kursi yang sudah dipesan
        kursi[kursi.index(no_kursi)] = "XX"
        
        # Tampilkan struk pemesanan
        print("=== Struk Pemesanan Tiket ===")
        print(f"Nama: {nama}")
        print(f"Nomor Kursi: {no_kursi}")
        print(f"Kategori: {kategori}")
        print(f"Harga: Rp{harga:,}")
        print(f"Password: {password}")
        print("=============================")
    else:
        print("Maaf, nomor kursi tidak valid atau sudah dipesan.")

# Tampilkan sisa kursi per kategori
print("Sisa kursi per kategori:")
for kategori, daftar_kursi in kategori_kursi.items():
    sisa = sum(1 for kursi in daftar_kursi if kursi != "XX")
    print(f"{kategori}: {sisa}")

# Tampilkan layout kursi setelah pemesanan
print("Layout Kursi Setelah Pemesanan:")
for i in range(baris):
    print(" ".join(kursi[i * kolom:(i + 1) * kolom]))

print("Terima kasih telah melakukan reservasi!")