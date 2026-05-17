in_file = input("Enter a file name: ")

try:
    buka = open(in_file)
except:
    print("File tidak ditemukan")
    quit()

itung_jam = dict()
for line in buka:
    if line.startswith("From "):
        parts = line.split()
        waktu = parts[5]
        jam = waktu.split(':')[0]
        itung_jam[jam] = itung_jam.get(jam, 0) + 1

hasil = sorted(itung_jam.items())
for jam, jumlah in hasil:
    print(jam, jumlah)
    