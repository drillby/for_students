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





app = QApplication([])
okno = Kalkukacka()
okno.show()
app.exec()
