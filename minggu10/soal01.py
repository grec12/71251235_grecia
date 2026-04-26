file1 = open('file1.txt', 'r', encoding='utf-8')
file2 = open('file2.txt', 'r', encoding='utf-8')

line1 = file1.readlines()
line2 = file2.readlines()

file1.close
file2.close

jumlah_baris = max(len(line1), len(line2))

for i in range(jumlah_baris):
    teks1 = line1[i].strip() if i < len(line1) else ''
    teks2 = line2[i].strip() if i < len(line2) else ''

    if teks1 == teks2:
        print(f"Baris {i+1} SAMA: {teks1}")
    else:
        print(f"Baris {i+1} BERBEDA: ")
        print(" file1:", teks1)
        print(" file2:", teks2)
    print()
