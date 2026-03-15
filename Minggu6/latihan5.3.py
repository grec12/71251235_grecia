def hitung_ips():
    bobot_nilai = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    sks_per_mk = 3
    total_sks = 0
    total_nilai = 0

    jumlah_mk =int(input("Masukkan jumlah mata kulia: "))

    for i in range(1, jumlah_mk + 1):
        while True:
            nilai = input(f"Masukkan nilai (A/B/C/D) untuk matakuliah ke-{i}: ").upper()
            if nilai in bobot_nilai:
                break
            print("Nilai tidak valid! masukkan A,B, C, atau D.")

        total_nilai += bobot_nilai[nilai] * sks_per_mk
        total_sks += sks_per_mk

    ips = total_nilai / total_sks
    print(f"\nNilai IPS ada semester ini {ips:.2f}")

hitung_ips()
