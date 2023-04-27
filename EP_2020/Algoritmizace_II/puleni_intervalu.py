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
    j = len(seznam) - 1

    while i <= j:
        pivot = (i + j) // 2

        if seznam[pivot] < cil:
            i = pivot + 1
        elif seznam[pivot] > cil:
            j = pivot - 1
        else:
            return pivot
    else:
        return -1


pole = [2, 7, 11, 31, 41, 56, 77, 101]

print(puleni_intervalu_i(pole, 12))

print(puleni_intervalu_r(pole, 12, 0, len(pole) - 1))
