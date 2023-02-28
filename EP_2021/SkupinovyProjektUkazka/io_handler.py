from os import PathLike
from typing import Generator


def get_io_type(is_input: bool) -> bool:
    """Zjistí jestli uživatel chce pracovat s terminálem, nebo souborem

    Args:
        is_input (bool): True, pokud chceme řešit input, output = False

    Returns:
        bool: True = práce s terminálem, False = práce se souborem
    """
    if is_input:
        vstup = ""
        while not vstup in ["1", "2"]:
            print("Chceš zadat čísla z konzole, nebo ze souboru?")
            print("1. Terminál")
            print("2. Soubor (input.txt)")
            vstup = input("Rozhodni se: ")

    else:
        vstup = ""
        while not vstup in ["1", "2"]:
            print("Chceš vypsat čísla do konzole, nebo do souboru?")
            print("1. Terminál")
            print("2. Soubor (input.txt)")
            vstup = input("Rozhodni se: ")

    return vstup == "1"



def output_to_file(output_file: PathLike, Fun: Generator[int, int, None], vstupni_cislo:int) -> None:
    """Vypíše čísla do souboru

    Args:
        output_file (PathLike): _description_
        Fun (Generator[int, int, None]): _description_
    """
    with open(output_file, "a") as f:
        # 15 -> 2, 3, 5, 7, 11, 13
        f.write(f"{vstupni_cislo} -> ")
        for i in Fun(int(vstupni_cislo)):
            f.write(f"{i}, ")
        f.write("\n")

def input_from_file(input_file: PathLike, Fun: Generator[int, int, None]):
    with open(input_file) as f:
        while True:
            radek = f.readline()
            if radek == "":
                break

            if not radek.replace("\n", "").isnumeric():
                radek = radek.replace('\n', '')
                print(f"Text {radek} nesplňuje podmínky")
                continue
            cislo = int(radek)
            print(f"Prvočísla do {cislo} jsou")
            for i in Fun(cislo):
                print(i)
            print("\n")