def pengecekan(tA):
    ada = tA[0]

    for elemen in tA:
        if elemen != ada:
            return False
    return True

tA = (90, 90, 90, 90)
print(pengecekan(tA))

