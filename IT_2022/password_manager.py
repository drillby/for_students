import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QPushButton, QLabel

class PasswordManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Seznam hesel")

        # Hlavní vertikální layout
        main_layout = QVBoxLayout()

        # List hesel
        self.list_widget = QListWidget()
        main_layout.addWidget(self.list_widget)

        # Horizontální layout pro vstupní pole
        input_layout = QHBoxLayout()

        # Popisek a pole pro jméno
        username_layout = QHBoxLayout()
        username_label = QLabel("Jméno:")
        self.username_input = QLineEdit()
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)

        # Popisek a pole pro heslo
        password_layout = QHBoxLayout()
        password_label = QLabel("Heslo:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)  # Zobrazí heslo jako hvězdičky
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)

        # Přidání polí do hlavního layoutu
        input_layout.addLayout(username_layout)
        input_layout.addLayout(password_layout)

        main_layout.addLayout(input_layout)

        # Tlačítko
        self.add_button = QPushButton("button")
        main_layout.addWidget(self.add_button)

        # Nastavení hlavního layoutu
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication([])
    window = PasswordManager()
    window.show()
    app.exec_()
