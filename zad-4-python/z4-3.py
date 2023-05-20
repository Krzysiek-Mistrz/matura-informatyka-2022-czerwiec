def pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def odbicie(n):
    return int(str(n)[::-1])

with open("../../informatyka-2022-zalaczniki/przyklad.txt", "r") as plik:
    liczby = [int(linia.strip()) for linia in plik]

print("4.3", end="\n")

for liczba in liczby:
    odwrocona = odbicie(liczba)
    if pierwsza(liczba) and pierwsza(odwrocona):
        print(liczba)

#oczywiscie takze jest podejscie alternatywne
"""
def pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
plikWyjscie = open('wynik4.txt', 'a')
plikWyjscie.write("4.3" + "\n")
for i in range(100):
    liczba = input()
    if pierwsza(int(liczba)) and pierwsza(int(reversed(liczba)))
        plikWyjscie.write(liczba + "\n")
plikWyjscie.close()
"""