def cetak_deret(tinggi, lebar):
    angka = 1
    for i in range(tinggi):
        baris = []
        for j in range(lebar):
            baris.append(str(angka))
            angka += 1
        print(" ".join(baris))

tinggi = int(input("Masukkan tinggi: "))
lebar = int(input("Masukkan tinggi: "))

cetak_deret(tinggi, lebar)
