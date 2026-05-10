filename = input("Masukkan nama file: ")
email_counts = {}

with open(filename, 'r') as file:
    for line in file:
        if line.startswith('From'):
            parts = line.split()
            email = parts[1]
            if email in email_counts:
                email_counts [email] += 1
            else:
                email_counts [email] = 1

print(email_counts)
