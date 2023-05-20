with open("../../informatyka-2022-zalaczniki/przyklad.txt", "r") as plik:
    liczby = [int(line.strip()) for line in plik]

print("4.4")

#zwraca od razu unikalne (dosyc podstawowa funkcja)
unikalne = set(liczby)
ileUnikalnych = len(unikalne)
print("Ile roznych liczb zapisano w pliku:", ileUnikalnych)

ile2 = 0
for liczba in unikalne:
    if liczby.count(liczba) == 2:
        ile2 += 1
    #lub (!duza zlozonosc obliczeniowa!):
    """
    for i in liczby:
        if liczba == i:
            ile2 += 1
    """
print("Ile liczb powtarza sie 2 razy w pliku: ", ile2)

ile3 = 0
for liczba in unikalne:
    if liczby.count(liczba) == 3:
        ile3 += 1
    #alternatywa podobna...
print("Ile liczb powtarza sie 3 razy w pliku:", ile3)
