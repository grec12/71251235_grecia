def perkalian (x, y):
    hasil_perkalian = x * y

    print(f"{x} x {y} = ", end=" ")
    print(" + ".join([str(y)] * x), end=" = ")
    print(hasil_perkalian)

perkalian(6, 5)
perkalian(7, 10)
