import random


def merge_sort(pole):
    if len(pole) > 1:
        # rozdělení na poloviny
        p = len(pole) // 2
        l_p = pole[:p]
        p_p = pole[p:]

        merge_sort(l_p)
        merge_sort(p_p)

        # Nyní máme podpole o jednom prvku každý

        i = j = k = 0

        while i < len(l_p) and j < len(p_p):
            if l_p[i] > p_p[j]:
                pole[k] = p_p[j]
                j += 1
            else:
                pole[k] = l_p[i]
                i += 1
            k += 1

        while i < len(l_p):
            pole[k] = l_p[i]
            i += 1
            k += 1

        while j < len(p_p):
            pole[k] = p_p[j]
            j += 1
            k += 1

    return pole


if __name__ == "__main__":
    pole = [random.randint(1, 500) for i in range(100)]
    print(pole)

    serazene_pole = merge_sort(pole)
    print(serazene_pole)
