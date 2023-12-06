import random
import time
from typing import List


def quick_sort(pole: List[int]):
    if len(pole) <= 1:
        return pole

    pivot = pole[0]
    leve = []
    prave = []

    for i in range(1, len(pole)):
        if pole[i] > pivot:
            leve.append(pole[i])
        else:
    #        prave.append(pole[i])

    #pole = pole[1:]
    #for prvek in pole:
    #    if prvek > pivot:
    #        leve.append(prvek)
    #    else:
    #        prave.append(prvek)

    #leve = [prvek for prvek in pole[1:] if prvek <= pivot]
    #prave = [prvek for prvek in pole[1:] if prvek > pivot]

    #leve = list(filter(lambda prvek: prvek < pivot, pole))
    #prave = list(filter(lambda prvek: prvek > pivot, pole))

    return quick_sort(leve) + [pivot] + quick_sort(prave)


if __name__ == "__main__":
    pole = [random.randint(1, 10_000) for _ in range(1_000_000)]
    print(pole)
    start = time.time()
    serazene = quick_sort(pole)
    konec = time.time()
    print(serazene)
    print("Doba trvání: ", konec - start)
