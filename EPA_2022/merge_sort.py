import random
import time

def merge_sort(pole):
    velikost = len(pole)
    if velikost > 1:
        prostredek = velikost // 2
        leve_pole = pole[:prostredek]
        prave_pole = pole[prostredek:]

        merge_sort(leve_pole)
        merge_sort(prave_pole)

        lp_index = 0 # index pro levé pole
        pp_index = 0 # index pro pravé pole
        sp_index = 0 # index pro nové, seřazené pole

        leva_delka = len(leve_pole)
        prava_delka = len(prave_pole)
        while lp_index < leva_delka and pp_index < prava_delka:
            if leve_pole[lp_index] < prave_pole[pp_index]:
                pole[sp_index] = leve_pole[lp_index]
                lp_index += 1
            else:
                pole[sp_index] = prave_pole[pp_index]
                pp_index += 1

            sp_index += 1

        while lp_index < leva_delka:
            pole[sp_index] = leve_pole[lp_index]
            lp_index += 1
            sp_index += 1

        while pp_index < prava_delka:
            pole[sp_index] = prave_pole[pp_index]
            pp_index += 1
            sp_index += 1



if __name__ == "__main__":
    pole = [random.randint(1, 10_000) for _ in range(1_000_000)]
	
    print(pole)
    start = time.time()
    merge_sort(pole)
    konec = time.time()
    print(pole)
    print("Doba trvání: ", konec - start)
