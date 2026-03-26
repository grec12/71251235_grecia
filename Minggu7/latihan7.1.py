def prim(v):
    if v < 2:
        return False
    for i in range (2, int (v**0.5) + 1):
        if v % i == 0:
            return False
    return True

def prima_terdekat(n):
    if n <= 2:
        prim(f"Tidak ada bilangan prima yang leboh kecil dari {n}")
        return
    for i in range (n - 1, 1, -1):
        if prim(i):
            return i

n = int(input("Masukkan niai v: "))
print(prima_terdekat(n))
