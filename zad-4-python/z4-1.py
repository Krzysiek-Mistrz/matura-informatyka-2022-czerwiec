def odbicie(n):
    return int(str(n)[::-1])

with open('../../informatyka-2022-zalaczniki/przyklad.txt', 'r') as file:
    liczby = [int(line.strip()) for line in file.readlines()]

odbicia = [odbicie(n) for n in liczby if odbicie(n) % 17 == 0]

print("4.1")

for i in odbicia:
    print(i)

#alternatywne podejscie
"""
plikWyjscie = open('wynik4.txt', 'w')
plikWyjscie.write("4.1" + "\n")
for i in range(100):
    liczba = int(reversed(input()))
    if not liczba % 17:
        plikWyjscie.write(str(liczba) + "\n")
plikWyjscie.close()
"""