def rata_rata():
    jumlah = 0
    count = 0

    while True:
        user_inp = input("Masukkan bilangan atau ketik 'done' untuk selesai: ")

        if user_inp.lower() == 'done':
            break

        if user_inp.replace('.', '', 1).isdigit():
            jumlah += float(user_inp)
            count += 1
        else:
            print("Input tidak valid")

    if count > 0:
        print(f"Rata-rata bilangan: {jumlah/count}")
    else:
        print("Tidak ada bilangan yang dimasukkan")

rata_rata()
