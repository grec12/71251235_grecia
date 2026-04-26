file_name = 'soal.txt'
print("nama file1:", file_name)

with open(file_name, 'r', encoding= 'utf-8') as file:
    for line in file:
        if '||' in line:
            soal, kunci = line.strip().split('||')
            soal = soal.strip()
            kunci = kunci.strip().lower()
            print(soal)
            answer = input("Jawab: ").strip().lower()
            if answer == kunci:
                print("Jawaban benar!\n")
            else:
                print("Jawaban salah!\n")

