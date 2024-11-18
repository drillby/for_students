# dostat znak z stisknutého tlačítka na QLine

from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QGridLayout
)


class Kalkukacka(QWidget):
    def __init__(self):
        super().__init__() # toto je zkrácený zápis stejného řádku v předchozí ukázce ḱódu
        self.rozlozeni = QVBoxLayout()
        self.grid = QGridLayout()
        self.setLayout(self.rozlozeni)
        self.radek = QLineEdit()
        self.rozlozeni.addWidget(self.radek)

        self.posledni_znak_eq = False

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
                print(1)
                self.radek.setText(priklad + znak)
                self.posledni_znak_eq = False
            elif znak == "=":
                print(2)
                self.vypocti_priklad(priklad, self.radek)
                self.posledni_znak_eq = False
            else:
                print(priklad)
                print(self.radek.text())
                self.radek.clear()
                print(self.radek.text())
                self.radek.setText(znak)
                self.posledni_znak_eq = False
        if znak == "=":
            self.vypocti_priklad(priklad, self.radek)
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
        out_widget.setText(vysledek)





app = QApplication([])
okno = Kalkukacka()
okno.show()
app.exec()
