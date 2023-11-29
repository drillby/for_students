import random
import time


def bubble_sort(pole: list[int]):
    delka_pole = len(pole)

    for i in range(delka_pole):
        for j in range(0, delka_pole - i - 1):
            if pole[j] < pole[j + 1]:
                pole[j], pole[j + 1] = pole[j + 1], pole[j]

    return pole


if __name__ == "__main__":
    pole = [random.randint(1, 10_000) for _ in range(10_000)]
    print(pole)
    start = time.time()
    setridene_pole = bubble_sort(pole)
    konec = time.time()
    print(setridene_pole)
    print("Doba trvání: ", konec - start)
