import numpy as np
from matplotlib import pyplot as plt

# Načtení dat

data = np.genfromtxt("./data/Prumerna_Teplota.csv", delimiter=";", dtype=str)

# Hlavička
headers = data[0]

# Samotná data
records = data[1:]

# Konstanty
POCET_DNI_V_MESICI = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MESICE = [
    "Leden",
    "Únor",
    "Březen",
    "Duben",
    "Květen",
    "Červen",
    "Červenec",
    "Srpen",
    "Září",
    "Říjen",
    "Listopad",
    "Prosinec",
]

# Funkce pro zpracování dat záznamů


def ziskej_teploty(zaznamy):
    """Získá teploty ze záznamů."""
    return [float(zaznam.split(",")[2]) for zaznam in zaznamy]


# Výpočet a vykreslení


def vykresli_graf(records):
    """Vykreslí graf pro každý měsíc."""
    iter_count = 0
    plt.figure(figsize=(15, 10))

    for index, pocet_dni in enumerate(POCET_DNI_V_MESICI):
        # Data pro aktuální měsíc
        zaznamy = records[iter_count : iter_count + pocet_dni]
        teploty = ziskej_teploty(zaznamy)
        dny = list(range(1, pocet_dni + 1))
        prumer_teplot = np.mean(teploty)

        # Subplot
        plt.subplot(3, 4, index + 1)
        plt.plot(dny, teploty, label="Denní teploty")
        plt.axhline(
            y=prumer_teplot,
            color="r",
            linestyle="--",
            label=f"Průměr: {prumer_teplot:.2f}°C",
        )

        plt.title(MESICE[index])
        plt.xlabel("Den")
        plt.ylabel("Teplota [°C]")
        plt.legend()

        iter_count += pocet_dni

    plt.tight_layout()
    plt.show()


# Volání funkce
vykresli_graf(records)
