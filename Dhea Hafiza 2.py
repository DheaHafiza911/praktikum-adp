print("================= Menghitung P(N(T) = n) =================")

lambda_t = float(input("Masukkan nilai lambda * t: "))
M = int(input("Masukkan nilai M : "))

e = 2.71828
n = 0
for n in range(M + 1):
    faktorial_n = 1
    for i in range(1, n + 1):
        faktorial_n *= i
    hasil = (e ** (-lambda_t) * (lambda_t ** n)) / faktorial_n
    print(f"P(N(t) = {n}) = {hasil}")
