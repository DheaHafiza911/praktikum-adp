n = int(input("Masukkan jumlah titik: "))
while n <= 0:
    print("Jumlah titik harus lebih dari 0!")
    n = int(input("Masukkan jumlah titik: "))


titik_list = []

for i in range(n):
    print(f"\nTitik ke-{i+1}")
    koordinat = input("Masukkan koordinat x y (pisah spasi): ")
    bagian = koordinat.split()
    x = float(bagian[0])
    y = float(bagian[1])
    titik_list.append([x, y])  

print("\nHasil Perhitungan:")
print("=" * 40)
print("No | Titik (x, y)       | Jarak dari (0,0)")
print("=" * 40)

for i in range(n):
    x, y = titik_list[i]
    jarak = (x**2 + y**2)**0.5
    print(f"{i+1:<2} | ({x:>6}, {y:>6})     | {jarak:>10.2f}")

print("=" * 40)
print("Program selesai!")
