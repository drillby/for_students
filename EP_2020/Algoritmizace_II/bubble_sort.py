from typing import List


def bubble_sort(pole: List[int]):
    delka_pole = len(pole)

    for i in range(delka_pole):
        for j in range(0, delka_pole - i - 1):
            if pole[j] < pole[j + 1]:
                pole[j], pole[j + 1] = pole[j + 1], pole[j]

    return pole


if __name__ == "__main__":
    pole = [-2, 59, 67, 3, 15]
    setridene_pole = bubble_sort(pole)
    print(setridene_pole)

    pole.sort()
    sorted(pole)
