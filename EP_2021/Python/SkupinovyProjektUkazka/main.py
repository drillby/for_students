import math
from typing import Generator


def erathosenovo_sito(hranice: int) -> Generator[int, int, None]:
    if hranice < 2:
        raise ValueError("Zadané číslo musí být větší než 2")

    sito = [True] * hranice  # [True, True, True, ...]

    for i in range(2, int(math.sqrt(hranice))):
        if sito[i]:
            for j in range(i * 2, hranice, i):
                sito[j] = False

    for cislo in range(hranice):
        if sito[cislo]:
            yield cislo

    # return [cislo for cislo in range(hranice) if sito[cislo]]

    # prvocisla = []
    # for cislo in range(hranice):
    #     if sito[i]:
    #         prvocisla.append(cislo)

    # return prvocisla


# for cislo in erathosenovo_sito(65):
#     print(cislo)


inp = ""
while inp not in ["1", "2"]:
    print("Chceš zadat číslo z klávesnice, nebo souboru?")
    print("1. Klávesnice")
    print("2. Soubor")
    inp = input("Rozhodni se... ")

if inp == "1":
    cislo = ""
    while not cislo.isnumeric():  # "12" -> True, "Pepa" -> False
        cislo = input("Zadej číslo větší než 2: ")
        if int(cislo) > 2:
            break

    for prvocislo in erathosenovo_sito(int(cislo)):
        print(prvocislo, end=", ")

# TODO: Zapisování do souboru, načítání ze souboru, rozodování pro zápis do souboru, nebo výpis do terminálu
