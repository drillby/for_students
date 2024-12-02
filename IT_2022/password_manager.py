from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QPushButton, QLabel, QListWidgetItem
import json

class PasswordManager(QWidget):
    def __init__(self):
        super().__init__()
        self.password_path = "./hesla.json"
        self.passwords = self.load_passwords(self.password_path)
        self.initUI()

    def load_passwords(self, path):
        with open(path, "r") as f:
            return json.load(f)

    def initUI(self):
        self.setWindowTitle("Seznam hesel")

        # Hlavní vertikální layout
        main_layout = QVBoxLayout()

        # List hesel
        self.list_widget = QListWidget()
        self.refresh_password_list(self.passwords)
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
        # self.password_input.setEchoMode(QLineEdit.Password)  # Zobrazí heslo jako hvězdičky
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)

        # Přidání polí do hlavního layoutu
        input_layout.addLayout(username_layout)
        input_layout.addLayout(password_layout)

        main_layout.addLayout(input_layout)

        # Tlačítko
        self.add_button = QPushButton("button")
        self.add_button.clicked.connect(self.save_password)
        main_layout.addWidget(self.add_button)

        # Nastavení hlavního layoutu
        self.setLayout(main_layout)

    def save_password(self):
        username = self.username_input.text()
        password = self.password_input.text()
        self.username_input.setText("")
        self.password_input.setText("")
        login_pair = {
            "username": username,
            "password": password
        }
        self.passwords.append(login_pair)
        with open(self.password_path, "w") as f:
            json.dump(self.passwords, f)
        self.refresh_password_list(self.passwords)


    def refresh_password_list(self, passwords):
        self.list_widget.clear()
        for login_pair in passwords:
            username = login_pair["username"]  # z json dostanem username
            password = login_pair["password"]  # z json dostanem password
            # pro každý username, heslo pair vytvoříme ListItem
            item = QListWidgetItem(f"Username: {username}")
            self.list_widget.addItem(item)
            # ještě přidáme funkci pro zobrazení detailu
if __name__ == "__main__":
    app = QApplication([])
    window = PasswordManager()
    window.show()
    app.exec_()
