import random
from PyQt5 import QtWidgets

app = QtWidgets.QApplication([]) # inicializace aplikace

hlavni_okno = QtWidgets.QWidget()  # vytvoření objektu hlavního okna
hlavni_okno.setWindowTitle("Můj supr program")  # název okna

usporadani = QtWidgets.QVBoxLayout() # vytvoření layoutu
hlavni_okno.setLayout(usporadani) # aplikace layoutu na hlavni_okno

napis = QtWidgets.QLabel("Nějaký text...") # vytvoření objektu napis
usporadani.addWidget(napis) # "nalepení" textu na hlavni_okno

napis_2 = QtWidgets.QLabel("Nějaký další text...") # vytvoření objektu napis
usporadani.addWidget(napis_2) # "nalepení" textu na hlavni_okno

tlacitko = QtWidgets.QPushButton("Klikni na mě...")
usporadani.addWidget(tlacitko)

text_pole = QtWidgets.QLineEdit()
usporadani.addWidget(text_pole)

pocetni_operace = QtWidgets.QLineEdit()
usporadani.addWidget(pocetni_operace)

def vyber_oparaci():
    # vytáhnutí početní operace z inputu
    operace = pocetni_operace.text()
    # roztřízení podle if/elif
    if operace == "+":
        # zavolání funkce
        # ! tady už se závorkami, jde nám o průběh ne o lokaci
        soucet()
        pocetni_operace.setText("")
    elif operace == "*":
        soucin()
        pocetni_operace.setText("")
    else:
        napis.setText("Neznámá operace")
        pocetni_operace.setText("")

    # match-case syntax Python3.10 a výš
    # match operace:
    #     case "+":
    #         ...
    #     case "*":
    #         ...
    #     case _:
    #         ...



def soucin():
    cisla_str = text_pole.text() # vytáhnutí textu z text_pole (vždy string)
    cisla_pole = cisla_str.split(" ") # 1 2 3 -> [1, 2, 3]

    # zjištění součinu
    vysledek = 1
    for cislo in cisla_pole:
        vysledek *= int(cislo)
    
    # nastavení nového textu na label napis
    napis.setText(f"Součin čísel {cisla_str} je {vysledek}")
    # vyčištění inputu
    text_pole.setText("")

def soucet():
    cisla_str = text_pole.text() # vytáhnutí textu z text_pole (vždy string)
    cisla_pole = cisla_str.split(" ") # 1a2a3 -> [1, 2, 3]
    vysledek = 0
    for cislo in cisla_pole:
        vysledek += int(cislo)
    
    # nastavení nového textu na label napis
    napis.setText(f"Součet čísel {cisla_str} je {vysledek}")
    # vyčištění inputu
    text_pole.setText("")

def vypis_text():
    a = text_pole.text() # vytáhnutí textu z text_pole (vždy string)
    # nastavení textu labelu napis_2 na hodnotu z inputu napis_2.setText(a)
    text_pole.setText("")

def nahodne_cislo():
    cislo = random.randint(0, 100) # generace náhodného čísla od 0 do 100
    napis.setText(str(cislo)) # nahrání čísla jako text do labelu napis 

# propojení tlačítka s požadovanou funkcí
# ! bez závorek, se závorkami by se fuknce vyhodnotila
tlacitko.clicked.connect(vyber_oparaci)

hlavni_okno.show() # okno bude viditelné

app.exec() # spuštění aplikace