import re

def cek_anagram(kata_pertama, kata_kedua):
    kata_pertama = re.sub(r"[^a-zA-Z]", "", kata_pertama).lower()
    kata_kedua = re.sub(r"[^a-zA-Z]", "", kata_kedua).lower()
    return sorted(kata_pertama) == sorted(kata_kedua)

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if cek_anagram(kata1, kata2):
    print(f"'{kata1}' dan '{kata2}' adalah anagram.")
else:
    print(f"'{kata1}' dan '{kata2}' bukan anagram")
    