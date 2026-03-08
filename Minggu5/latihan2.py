def cek_digit_belakang (a, b, c):
    digit_a = a % 10
    digit_b = b % 10
    digit_c = c % 10
    return (digit_a ==digit_b or digit_b == digit_c or digit_c == digit_a)

a = int(input("Masukkan angka: "))
b = int(input("Masukkan angka: "))
c = int(input("Masukkan angka: "))
hasil = cek_digit_belakang (a, b, c)
print (hasil)
