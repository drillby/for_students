from PyQt5 import QtWidgets
from PyQt5 import QtGui
import pygame

def animace_fib(pocet_prvku: int):
    pygame.init()
    CERNA = (0, 0, 0)
    MODRA = (0, 0, 255)
    BILA = (255, 255, 255)

    aktualni_prvek = 1

    pozice_stary = [10, 200]
    pozice_novy = [10, 400]

    velikost_ctverce = (5, 50)

    # Vytvoř okno pro hru
    velikost_okna = (800, 480)
    okno = pygame.display.set_mode(velikost_okna)
    okno.fill(BILA)

    # Nastav název okna
    pygame.display.set_caption("Animace Fibonacciho posloupnosti")

    # vytvoření objektu pro úpravu obnovovací frekvence
    hodiny = pygame.time.Clock()
    fps = 1

    # Nastav počáteční stav hry
    running = True
    
    # Hlavní herní smyčka
    while running:
        # Zpracuj události
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        if aktualni_prvek > pocet_prvku:
            continue
        stary, novy = fibi_pygame(aktualni_prvek)
        for i in range(stary): #5
            pygame.draw.rect(
            okno, CERNA, (*pozice_stary, *velikost_ctverce), 0
        )
            pozice_stary[0] = pozice_stary[0] + (2 * velikost_ctverce[0])
        for i in range(novy): # 8
            pygame.draw.rect(
            okno, MODRA, (*pozice_novy, *velikost_ctverce), 0
        )
            pozice_novy[0] = pozice_novy[0] + (2 * velikost_ctverce[0])
        
        # na konci jedné iterace nastavíme začísající pozici další iterace
        # děláme to z důvodu aby byly rozlišeny jednotlivé kroky
        pozice_novy[0] = pozice_novy[0] + (4*velikost_ctverce[0])
        pozice_stary[0] = pozice_novy[0]
        aktualni_prvek += 1

        hodiny.tick(fps)
        pygame.display.flip()

    # Ukonči PyGame
    pygame.quit()


def fibi_pygame(n: int):
    # nový prvek = součet dvou předchozích
    # začátek posloupnosti 0, 1
    if n <= 0:
        raise ValueError("n musí být větší než 0")

    stary = 0
    novy = 1

    if n == 1 or n == 2:
        return stary, novy

    for _ in range(2, n+1):
        # nová hodnota "stary" = puvodní hodnota "novy"
        # nová hodnota "novy" = součet "novy" a "stary"
        stary, novy = novy, novy + stary
    return stary, novy

def fibi_pyqt(n: int) -> int:
    # nový prvek = součet dvou předchozích
    # začátek posloupnosti 0, 1
    if n <= 0:
        raise ValueError("n musí být větší než 0")

    stary = 0
    novy = 1

    if n == 1:
        return stary
    if n == 2:
        return novy

    for _ in range(2, n+1):
        # nová hodnota "stary" = puvodní hodnota "novy"
        # nová hodnota "novy" = součet "novy" a "stary"
        stary, novy = novy, novy + stary
    return novy

def zjisti_cislo():
    text = chteny_prvek.text()
    return int(text)

def wrapper_pyqt():
    cislo = zjisti_cislo()
    if cislo <= 0:
        vysledek.setText(f"Musíš zadat číslo větší než 0")
        return
    prvek = fibi_pyqt(cislo)
    vysledek.setText(f"Prvek {cislo} Fibonacciho posloupnosti je {prvek}")

def wrapper_pygame():
    cislo = zjisti_cislo()
    if cislo <= 0:
        vysledek.setText(f"Musíš zadat číslo větší než 0")
        return
    animace_fib(cislo)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])  # inicializace aplikace

    hlavni_okno = QtWidgets.QWidget()  # vytvoření objektu hlavního okna
    hlavni_okno.setWindowTitle("Fibonacciho posloupnost")  # název okna

    usporadani = QtWidgets.QVBoxLayout()  # vytvoření layoutu
    hlavni_okno.setLayout(usporadani)  # aplikace layoutu na hlavni_okno

    napis = QtWidgets.QLabel("Kolikátý prvek posloupnoti chceš zjistit?")  # vytvoření objektu napis
    usporadani.addWidget(napis)  # "nalepení" textu na hlavni_okno

    validator_celych_cisel = QtGui.QIntValidator()  # Validátor vstupních hodnot - nastavený na kontrolu celých čísel
    chteny_prvek = QtWidgets.QLineEdit()
    chteny_prvek.setValidator(validator_celych_cisel)  # přidání validátoru na objekt
    usporadani.addWidget(chteny_prvek)

    vysledek = QtWidgets.QLabel("Ještě jsi nic nezadal")  # vytvoření objektu napis
    usporadani.addWidget(vysledek)  # "nalepení" textu na hlavni_okno
    tlacitko = QtWidgets.QPushButton("Klikni na mě...")
    usporadani.addWidget(tlacitko)
    tlacitko_2 = QtWidgets.QPushButton("Spustit animaci")
    usporadani.addWidget(tlacitko_2)
    # propojení tlačítka s požadovanou funkcí
    # ! bez závorek, se závorkami by se fuknce vyhodnotila
    tlacitko.clicked.connect(wrapper_pyqt)
    tlacitko_2.clicked.connect(wrapper_pygame)

    hlavni_okno.show()  # okno bude viditelné

    app.exec()  # spuštění aplikace