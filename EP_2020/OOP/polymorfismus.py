from typing import List, Union

def secti(param1: int, param2: int):
    return param1 + param2

def secti2(param1: Union[int, float, str, list], param2: Union[int, float]):
    return param1 + param2

class Dopravce:
    def cena_za_km(pocet_km):
        ...

    def celkova_cena(cenaza_kms, poplatky):
        ...


class PPL:
    def cena_za_km(pocet_km):
        return 50 * pocet_km

    def celkova_cena(cenaza_kms, poplatky):
        return cenaza_kms + poplatky

class CeskaPosta:
    def cena_za_km(pocet_km):
        return 60 * pocet_km

    def celkova_cena(cenaza_kms, poplatky):
        return cenaza_kms + 2*poplatky

def vyber_nejlevnejsi(dopravce: List[Dopravce]):
    for dop in dopravce:
        cena_za_km = dop.cena_za_km(20)
        cel_cena = dop.celkova_cena(cena_za_km, 200)
        print(cel_cena)



if __name__ == "__main__":
    dopravce = (PPL, CeskaPosta)
    vyber_nejlevnejsi(dopravce)