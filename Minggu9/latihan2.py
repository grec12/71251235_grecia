import re

def hitung_kata(teks, kata_dicari):
    teks = re.sub(r"[^\w\s]", "", teks).lower()
    kata_dicari = kata_dicari.lower()
    list_kata = teks.split()
    total = list_kata.count(kata_dicari)
    return total

kal =input("Masukkan kalimat yang diinginkan: ")
kata = input("Masukkan kata yang ingin dihitung: ")

frekuensi = hitung_kata(kal, kata)
print(f"'{kata}' dan {frekuensi} buah.")

