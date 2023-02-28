from os import PathLike
from typing import Generator

import e_sito
import io_handler

def main() -> None:
    is_input = True
    vstup = io_handler.get_io_type(is_input)

    is_input = False
    vystup = io_handler.get_io_type(is_input)

    if vstup:
        cislo = ""
        while not cislo.isnumeric():
            cislo = input("Zadej číslo: ")

        if vystup:
            cislo = int(cislo)
            if cislo < 2:
                print("Číslo musí být větší než 2, zkus to znovu...")
            else:
                for i in e_sito.eratosthenovo_sito(cislo):
                    print(i)
        else:
            # zapsání do souboru
            output_file = "prvocisla.txt"
            io_handler.output_to_file(output_file, e_sito.eratosthenovo_sito, cislo)
    else:
        input_file = "input.txt"
        if vystup:
            io_handler.input_from_file(input_file, e_sito.eratosthenovo_sito)
        else:
            with open(input_file) as fi:
                while True:
                    radek = fi.readline()
                    if radek == "":
                        break

                    if not radek.replace("\n", "").isnumeric():
                        continue
                    cislo = int(radek)
                    if cislo < 2:
                        continue

                    # zapsání do souboru
                    output_file = "prvocisla.txt"
                    io_handler.output_to_file(output_file, e_sito.eratosthenovo_sito, cislo)


if __name__ == "__main__":
    main()
