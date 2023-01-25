cislo = input("Zadej číslo: ")

try:
    "text" + 2
    print(int(cislo) * 2)
except Exception:
    print("Slovo nelze předělat na int.")