print("===================DAFTAR MENU MAKANAN===================")
print("  | Paket |              Isi               |   Harga   | ")
print("1.|   A   | Nasi goreng,Es teh             | Rp.30.000 | ")
print("2.|   B   | Ayam bakar,Nasi Putih,Es Jeruk | Rp.50.000 | ")
print("3.|   C   | Ayam Geprek,Es Jeruk           | Rp.45.000 | ")
print("4.|   D   | Ikan bakar,Nasi Putih,Es Teh   | Rp.50.000 | ")
print("5.|   E   | Mie Goreng,Es Jeruk            | Rp.35.000 | ")
print("=========================================================")

nama = input("Nama: ")
no_telepon = input("Nomor Telepon: ")
alamat = input("Alamat Pengiriman: ")

pilihan = int(input("Pilih paket (1-5): "))
jumlah = int(input("Jumlah paket: "))

harga_paket = [30000, 50000, 45000, 50000, 45000]
total_harga = harga_paket[pilihan - 1] * jumlah
pajak = total_harga * 0.10

if total_harga < 150000:
    biaya_pengiriman = 25000
else:
    biaya_pengiriman = 0

paket_makanan = {
    1: "Nasi Goreng, Es Teh",
    2: "Ayam Bakar, Nasi Putih, Es Jeruk",
    3: "Ayam Geprek, Es Jeruk",
    4: "Ikan Bakar, Nasi Putih, Es Teh",
    5: "Mie Goreng, Es Jeruk"
    }

huruf_paket = ["A", "B", "C", "D", "E"] # Daftar huruf paket

print("================ Struk Pemesanan ================")
print("Nama:", nama)
print("Nomor Telepon:", no_telepon)
print("Alamat Pengiriman:", alamat)
print("\nDetail Pesanan:")
print(f"Paket {huruf_paket[pilihan -1]}: {paket_makanan[pilihan]}") #Menggunakan list huruf_paket
print("Jumlah:", jumlah)
print("Total Harga: Rp", total_harga)
print("Pajak (10%): Rp", pajak)
print("Biaya Pengiriman: Rp", biaya_pengiriman)
print("Total Akhir: Rp", total_harga + pajak + biaya_pengiriman)
print("=================================================")