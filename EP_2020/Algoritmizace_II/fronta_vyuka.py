from typing import Any


class Bunka:
    def __init__(self, msg: Any, dalsi_bunka) -> None:
        self.zprava = msg
        self.dalsi_bunka = dalsi_bunka

    def __str__(self) -> str:
        return f"Buňka se zprávou: {self.zprava}"


class Fronta:
    def __init__(self) -> None:
        self.pocet_prvku = 0
        self.prvni_bunka = None

    def pridej(self, nova_bunka: Bunka) -> None:
        nova_bunka.dalsi_bunka = self.prvni_bunka
        self.prvni_bunka = nova_bunka
        self.pocet_prvku += 1

    def odeber(self):
        if self.pocet_prvku == 0:
            raise IndexError("Fronta je prázdná")

        elif self.pocet_prvku == 1:
            posledni_bunka = self.prvni_bunka
            self.prvni_bunka = None
            self.pocet_prvku -= 1
            return posledni_bunka

        else:
            aktualni_bunka = self.prvni_bunka
            predposledni_bunka = None
            while aktualni_bunka.dalsi_bunka is not None:
                predposledni_bunka = aktualni_bunka
                aktualni_bunka = aktualni_bunka.dalsi_bunka

            predposledni_bunka.dalsi_bunka = None
            self.pocet_prvku -= 1
            return aktualni_bunka

    def vypis_bunky(self) -> None:
        print("=== Začátek ===")
        aktualni_bunka = self.prvni_bunka
        while aktualni_bunka is not None:
            print(aktualni_bunka)
            aktualni_bunka = aktualni_bunka.dalsi_bunka
        print("=== Konec ===")


if __name__ == "__main__":
    B1 = Bunka("První", None)
    B2 = Bunka("Druhá", None)
    B3 = Bunka("Třetí", None)
    B4 = Bunka("Čtvrtá", None)
    B5 = Bunka("Pátá", None)

    F1 = Fronta()
    F1.pridej(B1)
    F1.pridej(B2)
    F1.pridej(B3)
    F1.vypis_bunky()
    F1.pridej(B4)
    F1.vypis_bunky()

    print("Odebírám: ", F1.odeber())
    print("Odebírám: ", F1.odeber())
    F1.vypis_bunky()
    F1.pridej(B5)
    F1.vypis_bunky()

    print("Odebírám: ", F1.odeber())
    print("Odebírám: ", F1.odeber())
    print("Odebírám: ", F1.odeber())
    F1.vypis_bunky()

    print("Odebírám: ", F1.odeber())
