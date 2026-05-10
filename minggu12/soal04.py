filename = input("Masukkan nama file: ")
domain_counts = {}

with open(filename, 'r') as file:
    for line in file:
        if line.startswith('From'):
            parts = line.split()
            email = parts[1]
            domain = email.split('@')[1]
            if domain in domain_counts:
                domain_counts [domain] += 1
            else:
                domain_counts [domain] = 1

print(domain_counts)
