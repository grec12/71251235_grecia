def cek_angka (a, b, c):
    if a != b and a != c and b != c:
        if a + b == c or b + c == a or c + a == b:
            return("True")
    return("False")

print (cek_angka(9, 5, 7))
print (cek_angka(2, 3, 1))
print (cek_angka(4, 3, 2))