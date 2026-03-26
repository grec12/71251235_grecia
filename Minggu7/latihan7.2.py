import math
n = int(input("Masukkan nilai n: "))

for i in range(n, 0, -1):
    faktorial = math.factorial(i)
    print(faktorial, end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
    