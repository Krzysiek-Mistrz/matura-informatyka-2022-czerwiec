def odbicie(n):
    return int(str(n)[::-1])

with open("../../informatyka-2022-zalaczniki/przyklad.txt", "r") as plik:
    liczby = [int(linia.strip()) for linia in plik]

maxRoznica = -1000
maxNumer = 0

for n in liczby:
    roznica = abs(n - odbicie(n))
    if roznica > maxRoznica:
        maxRoznica = roznica
        maxNumer = n

print("4.2", end="\n")
print(f"Najwieksza roznica dla liczby {maxNumer} wynosi {maxRoznica}")

#alternatywne podejscie podobne jak poprzednio
"""
plikWyjscie = open('wynik4.txt', 'a')
plikWyjscie.write("4.2" + "\n")
maxLiczba = 0
maxRoznica = -1000
for i in range(100):
    liczba = input()
    roznica = abs(int(liczba) - int(reversed(liczba))
    if roznica > maxRoznica:
        maxRoznica = roznica
        maxNumer = int(liczba)
plikWyjscie.write(str(maxRoznica) + " " + str(maxLiczba) + "\n")
plikWyjscie.close()
"""