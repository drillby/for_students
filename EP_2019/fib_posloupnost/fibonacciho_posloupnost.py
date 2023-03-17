from PyQt5 import QtWidgets
from PyQt5 import QtGui
import pygame

def fibonnaci(x):
    if x < 1:
        raise ValueError("Pořadí menší než 1")
    v = 1
    p = 1
    q = 1

    for i in range(0, x-2):  # x-2 krát zopakuj
        v = p+q
        p = q
        q = v

    return v


def fibonnaci_podrobne(krok):
    if krok < 1:
        raise ValueError("Krok menší než 1")
    stari = 0
    novy = 1

    for i in range(0, krok-1):  # x-1 krát zopakuj
        pomocna = stari
        stari = stari + novy
        novy = pomocna

    return stari, novy


def nakresli_kraliky(kolik, start_x, start_y, platno, barva):
    od = [start_x, start_y]
    do = [start_x, start_y+50]
    mezera = 10
    for i in range(kolik):
        pygame.draw.line(platno, barva, od, do, 3)
        od[0] += mezera
        do[0] += mezera


def graficke_zobrazeni():
    pygame.init()

    vstupni_hodnota = int(vstup.text())

    display_width = 800
    display_height = 200

    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Zobrazení Fibonacciho posloupnosti')

    black = (0, 0, 0)  # RGB+Alpha (Alpha - průhlednost)
    white = (255, 255, 255)
    blue = (0, 0, 255)

    zacatek = 50
    posun = 100

    screen.fill(white)

    hodiny = pygame.time.Clock()
    fps = 1
    krok = 1
    running = True
    while running:
        # do fronty událostí pygame.event.get() se ukládají všechny události v průběhu jednoho frame
        # události -> start, quit, zmáčknutí klávesy, klik myší, pohyb myší, ...
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if krok <= vstupni_hodnota:
            stare, nove = fibonnaci_podrobne(krok)
            krok += 1

            nakresli_kraliky(stare, zacatek, 50, screen, black)
            nakresli_kraliky(nove, zacatek, 110, screen, blue)
            zacatek += posun

            pygame.display.update()

        hodiny.tick(fps)

    pygame.quit()


app = QtWidgets.QApplication([])

hlavni_okno = QtWidgets.QWidget()
hlavni_okno.setWindowTitle('Fibonnaci')

usporadani = QtWidgets.QVBoxLayout()
hlavni_okno.setLayout(usporadani)

# validator_celych_cisel = QtGui.QIntValidator()  # 1/2 Možnost jak zabránit napsání něčeho, co není Integer
vstup = QtWidgets.QLineEdit()
# vstup.setValidator(validator_celych_cisel)  # 2/2 do vstupu
usporadani.addWidget(vstup)

tlacitko = QtWidgets.QPushButton('Ukaž hodnotu')
usporadani.addWidget(tlacitko)

napis = QtWidgets.QLabel('Výsledek: ...')
usporadani.addWidget(napis)

tlacitko_graficke = QtWidgets.QPushButton('Zobraz graficky')
usporadani.addWidget(tlacitko_graficke)


def spocitej():
    try:
        vstupni_hodnota = int(vstup.text())
        vysledek = fibonnaci(vstupni_hodnota)
    except ValueError:
        vysledek = "Zadej číslo 1-nekonečno"

    napis.setText("Prvek {} fibbonaciho posloupnosti má hodnotu {}".format(
        vstupni_hodnota, vysledek))


tlacitko.clicked.connect(spocitej)
tlacitko_graficke.clicked.connect(graficke_zobrazeni)

hlavni_okno.show()

app.exec()
