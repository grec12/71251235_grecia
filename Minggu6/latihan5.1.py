def ganjil(bawah, atas):
    if bawah < atas:
        return [i for i in range (bawah, atas + 1) if i % 2 == 1]
    else:
        return [i for i in range (bawah, atas - 1, -1) if i % 2 == 1]

bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))

hasil =ganjil(bawah, atas)
print ("Deret bilangan ganjil: ", hasil)
