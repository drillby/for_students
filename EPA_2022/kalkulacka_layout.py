import sys

from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

# Vytvoření aplikace
app = QApplication(sys.argv)

# Hlavní okno


class Kalkukacka(QWidget):
    def __init__(self):
        super().__init__()

        # Nastavení okna
        self.setWindowTitle("Kalkulačka")

        # Hlavní vertikální layout
        main_layout = QVBoxLayout()

        # Displej
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setText("0")
        self.display.setStyleSheet("font-size: 24px;")
        main_layout.addWidget(self.display)

        # Mřížkový layout pro tlačítka
        button_layout = QGridLayout()

        # Tlačítka
        buttons = [
            ("H", 0, 0),
            ("CE", 0, 1),
            ("C", 0, 2),
            ("⌫", 0, 3),
            ("1/x", 1, 0),
            ("x²", 1, 1),
            ("√", 1, 2),
            ("/", 1, 3),
            ("7", 2, 0),
            ("8", 2, 1),
            ("9", 2, 2),
            ("*", 2, 3),
            ("4", 3, 0),
            ("5", 3, 1),
            ("6", 3, 2),
            ("-", 3, 3),
            ("1", 4, 0),
            ("2", 4, 1),
            ("3", 4, 2),
            ("+", 4, 3),
            ("0", 5, 0, 1, 2),
            (".", 5, 2),
            ("=", 5, 3),
        ]

        for text, row, col, *span in buttons:
            button = QPushButton(text)
            button.setStyleSheet("font-size: 18px; height: 40px;")
            button.clicked.connect(self.on_click)
            if span:
                button_layout.addWidget(button, row, col, *span)
            else:
                button_layout.addWidget(button, row, col)

        # Přidání mřížkového layoutu do hlavního layoutu
        main_layout.addLayout(button_layout)

        # Nastavení hlavního layoutu
        self.setLayout(main_layout)

        self.priklad = ""

    def on_click(self):
        button = self.sender()
        text = button.text()

        if text == "C":
            self.display.setText("")
            self.priklad = ""
        if text == "=":
            # Výpočet
            try:
                vysledek = eval(self.priklad)
                self.display.setText(str(vysledek))
            except Exception:
                self.display.setText("Chyba")

        whitelist = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "x²", "1/x")
        if text in whitelist:
            



# Vytvoření instance hlavního okna
kalkulacka = Kalkukacka()
kalkulacka.show()

# Spuštění aplikace
sys.exit(app.exec_())
