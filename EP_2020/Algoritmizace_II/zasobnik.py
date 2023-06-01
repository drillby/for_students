class Bunka:
    def __init__(self, zprava):
        self.zprava = zprava
        self.dalsi_bunka = None

    def __str__(self):
        return "Bunka se zpravou: " + self.zprava


class Zasobnik:
    def __init__(self):
        self.velikost = 0
        self.prvni_bunka = None

    def pridej(self, nova_bunka: Bunka):
        nova_bunka.dalsi_bunka = self.prvni_bunka
        self.prvni_bunka = nova_bunka
        self.velikost += 1

    def odeber(self):
        if self.velikost == 0:
            raise IndexError("Zásobník je prázdný")
        else:
            aktualni_bunka = self.prvni_bunka
            self.prvni_bunka = self.prvni_bunka.dalsi_bunka
            self.velikost -= 1
            return aktualni_bunka

    def vypis_vsechny_bunky(self):
        print("=== Začátek ===")
        aktualni = self.prvni_bunka
        while aktualni is not None:
            print(aktualni)
            aktualni = aktualni.dalsi_bunka
        print("=== Konec ===")


if __name__ == "__main__":
    B1 = Bunka("Prvni")
    B2 = Bunka("Druha")
    B3 = Bunka("Treti")
    B4 = Bunka("Ctvrta")

    Z1 = Zasobnik()
    Z1.pridej(B1)
    Z1.pridej(B2)
    Z1.pridej(B3)
    Z1.vypis_vsechny_bunky()
    Z1.pridej(B4)
    Z1.vypis_vsechny_bunky()
    print("Odebírám: ", Z1.odeber())
    Z1.vypis_vsechny_bunky()
    print("Odebírám: ", Z1.odeber())
    print("Odebírám: ", Z1.odeber())
    Z1.vypis_vsechny_bunky()
