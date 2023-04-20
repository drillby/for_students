import random
from typing import List


def quick_sort(pole: List[int]):
    if len(pole) <= 1:
        return pole

    pivot = pole[0]
    leve = []
    prave = []

    for i in range(1, len(pole)):
        if pole[i] < pivot:
            leve.append(pole[i])
        else:
            prave.append(pole[i])

    return quick_sort(leve) + [pivot] + quick_sort(prave)


if __name__ == "__main__":
    pole = [random.randint(1, 100) for _ in range(100)]
    print(pole)
    serazene = quick_sort(pole)
    print(serazene)
