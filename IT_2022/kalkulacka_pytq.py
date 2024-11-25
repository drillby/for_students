# dostat znak z stisknutého tlačítka na QLine

from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QGridLayout,
    QListWidget,
    QListWidgetItem,
    QMessageBox
)

import os


class Kalkukacka(QWidget):
    def __init__(self, historie_widget):
        super().__init__() # toto je zkrácený zápis stejného řádku v předchozí ukázce ḱódu
        self.rozlozeni = QVBoxLayout()
        self.grid = QGridLayout()
        self.setLayout(self.rozlozeni)
        self.radek = QLineEdit()
        self.rozlozeni.addWidget(self.radek)

        self.posledni_znak_eq = False

        self.historie = historie_widget()

        self.rozlozeni.addLayout(self.grid)
        self.znaky = [
            ["(", ")", "H", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["+/-", "0", ".", "="]
        ]

        for x, radek in enumerate(self.znaky):
            for y, znak in enumerate(radek):
                tlacitko = QPushButton(znak)
                self.grid.addWidget(tlacitko, x, y)
                tlacitko.clicked.connect(self.zpracuj_znak)


    def zpracuj_znak(self):
        tlacitko = self.sender()
        znak = tlacitko.text()
        priklad = self.radek.text()
        if self.posledni_znak_eq:
            if znak in "+-*/":
                self.radek.setText(priklad + znak)
                self.posledni_znak_eq = False
            elif znak == "=":
                self.vypocti_priklad(priklad, self.radek)
                self.posledni_znak_eq = False
            elif znak == "H":
                self.historie.vypis()
                self.historie.show()
            else:
                self.radek.clear()
                self.radek.setText(znak)
                self.posledni_znak_eq = False
        elif znak == "=":
            self.vypocti_priklad(priklad, self.radek)
        elif znak == "H":
            self.historie.vypis()
            self.historie.show()
        else:
            self.radek.setText(priklad+znak)


    def vypocti_priklad(self, priklad, out_widget):
        povolene_znaky = "0123456789+-*/()"
        for znak in priklad:
            if not (znak in povolene_znaky):
                out_widget.setText("Nepovolený znak")
                return

        prvni_znak = priklad[0]
        posledni_znak = priklad[-1]
        if prvni_znak in "*/" or posledni_znak in "+-*/":
            out_widget.setText("Nepovolená sekvence znaků")
            return

        zasobnik = []
        for znak in priklad:
            if znak == "(":
                zasobnik.append("(")
            elif znak == ")":
                if not zasobnik:
                    out_widget.setText("Chybí '('")
                    return
                zasobnik.pop()

        if zasobnik:
            out_widget.setText("Chybí ')")
            return
        vysledek = str(eval(priklad))
        self.posledni_znak_eq = True
        self.historie.pridej(priklad + "=" + vysledek + "\n")
        out_widget.setText(vysledek)


class Historie(QWidget):
    def __init__(self):
        super().__init__()
        self.rozlozeni = QVBoxLayout()
        self.setLayout(self.rozlozeni)
        self.listWidget = QListWidget()
        self.rozlozeni.addWidget(self.listWidget)

    def vypis(self):
        self.listWidget.clear()
        if not os.path.isfile("historie.txt"):
            QMessageBox.warning(self, "Chyba", "Soubor 'historie.txt' neexistuje")
            return
        with open("historie.txt", "r") as f:
            historie = f.readlines()
            for priklad in historie:
                listWidgetItem = QListWidgetItem(priklad)
                self.listWidget.addItem(listWidgetItem)

    def pridej(self, priklad):
        with open("historie.txt", "a") as f:
            f.write(priklad)

app = QApplication([])
okno = Kalkukacka(Historie)
okno.show()
app.exec()
