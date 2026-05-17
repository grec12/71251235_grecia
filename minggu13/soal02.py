data = ('Matahari Bhakti Nendya', '22064091', 'Bantul, DIYogyakarta')

print("NIM    : ", data[1])
print("NAMA   : ", data[0])
print("ALAMAT : ", data[2])

nim = tuple(data[1])
print("\nNIM: ", nim)

nama_depan = tuple(data[0].split()[0])
print("NAMA DEPAN: ", nama_depan[1:])

nama_terbalik = tuple(reversed(data[0].split()))
print("NAMA TERBALIK: ", nama_terbalik)

