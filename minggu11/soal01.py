def tiga_bilangan_terbaik(lst):
    unique_num = set(lst)
    sorted_num = sorted(unique_num, reverse=True)
    return sorted_num[:3]

def main():
    bilangan = []
    print("Masukkan 3 bilangan satu per satu: ")

    for i in range(3):
        while True:
            try:
                number = int(input(f"Input bilangan ke-{i+1}: "))
                bilangan.append(number)
                break
            except ValueError:
                print("Input harus berupa bilangan bulat valid, coba lagi.")

    terbaik = tiga_bilangan_terbaik(bilangan)
    print("3 bilangan terbaik adalah:", terbaik)

if __name__ == "__main__":
    main()
    