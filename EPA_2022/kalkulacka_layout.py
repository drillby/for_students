from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout
import sys

# Vytvoření aplikace
app = QApplication(sys.argv)

# Hlavní okno
window = QWidget()
window.setWindowTitle("Kalkulačka")

# Hlavní vertikální layout
main_layout = QVBoxLayout()

# Displej
display = QLineEdit()
display.setReadOnly(True)
display.setText("0")
display.setStyleSheet("font-size: 24px;")
main_layout.addWidget(display)

# Mřížkový layout pro tlačítka
button_layout = QGridLayout()

# Tlačítka
buttons = [
    ('%', 0, 0), ('CE', 0, 1), ('C', 0, 2), ("⌫", 0, 3),
    ('1/x', 1, 0), ('x²', 1, 1), ('√', 1, 2), ('/', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0, 1, 2), ('.', 5, 2), ('=', 5, 3)
]

for text, row, col, *span in buttons:
    button = QPushButton(text)
    button.setStyleSheet("font-size: 18px; height: 40px;")
    if span:
        button_layout.addWidget(button, row, col, *span)
    else:
        button_layout.addWidget(button, row, col)

# Přidání mřížkového layoutu do hlavního layoutu
main_layout.addLayout(button_layout)

# Nastavení hlavního layoutu
window.setLayout(main_layout)

# Zobrazení okna
window.show()

# Spuštění aplikace
sys.exit(app.exec_())
