import random
import time
from typing import List


def puleni_intervalu_r(seznam: List[int], cil: int, min: int, max: int) -> int:
    if max < min:
        return -1
    stred = min + ((max - min) // 2)
    if seznam[stred] == cil:
        return stred
    if cil < seznam[stred]:
        return puleni_intervalu_r(seznam, cil, min, stred - 1)
    else:
        return puleni_intervalu_r(seznam, cil, stred + 1, max)


def puleni_intervalu_i(seznam: List[int], cil: int):
    i = 0
    j = len(seznam)

    while i < j:
        pivot = (i + j) // 2

        if seznam[pivot] < cil:
            i = pivot
        elif seznam[pivot] > cil:
            j = pivot
        else:
            return pivot
    else:
        return -1


def linearni_vyhledavani(seznam: List[int], cil: int) -> int:
    for idx, prvek in enumerate(seznam):
        if prvek == cil:
            return idx
    return -1


if __name__ == "__main__":
    print("Generuji pole")
    pole = [random.randint(1, 10_000) for i in range(30_000_000)]
    pole.sort()
    print("Pole seřazeno")

    start = time.perf_counter()
    time.perf_counter()
    vysledek = puleni_intervalu_i(pole, 12)
    konec = time.perf_counter()
    print("Půlení intervalů iterativně trvalo ", konec - start)
    print("Číslo bylo nalezeno na indexu ", vysledek)

    start = time.perf_counter()
    puleni_intervalu_r(pole, 12, 0, len(pole))
    konec = time.perf_counter()
    print("Půlení intervalů rekurzivně trvalo ", konec - start)
    print("Číslo bylo nalezeno na indexu ", vysledek)

    start = time.perf_counter()
    linearni_vyhledavani(pole, 12)
    konec = time.perf_counter()
    print("Lineární vyhledávání trvalo ", konec - start)
    print("Číslo bylo nalezeno na indexu ", vysledek)
