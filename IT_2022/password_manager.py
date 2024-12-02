from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QPushButton, QLabel, QListWidgetItem, QMessageBox
import json
import string


class PasswordManager(QWidget):
    def __init__(self):
        super().__init__()
        self.password_path = "./hesla.json"
        self.passwords = self.load_passwords(self.password_path)
        self.initUI()

        self.MIN_LEN = 10
        self.HAS_NUM = False
        self.HAS_SPECIAL_CHARS = True

    def load_passwords(self, path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def initUI(self):
        self.setWindowTitle("Seznam hesel")

        # Hlavní vertikální layout
        main_layout = QVBoxLayout()

        # List hesel
        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.show_detail)  # Při kliknutí na položku zobrazíme detail
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
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)

        # Přidání polí do hlavního layoutu
        input_layout.addLayout(username_layout)
        input_layout.addLayout(password_layout)

        main_layout.addLayout(input_layout)

        # Tlačítko
        self.add_button = QPushButton("Přidat heslo")
        self.add_button.clicked.connect(self.save_password)
        main_layout.addWidget(self.add_button)

        # Nastavení hlavního layoutu
        self.setLayout(main_layout)

    def save_password(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if not username or not password:
            QMessageBox.warning(self, "Chyba", "Zadejte uživatelské jméno a heslo.")
            return
        if not self.check_password_strength(password, self.MIN_LEN, self.HAS_NUM, self.HAS_SPECIAL_CHARS):
            QMessageBox.warning(self, "Chyba", f"Heslo nesplňuje zadané požadavky\nMinimální délka: {self.MIN_LEN}\nMá obsahovat čísla: {'Ano' if self.HAS_NUM else 'Ne'}\nMá obsahovat speciální znaky: {'Ano' if self.HAS_SPECIAL_CHARS else 'Ne'}")
            return
        self.username_input.setText("")
        self.password_input.setText("")
        login_pair = {"username": username, "password": password}
        self.passwords.append(login_pair)
        with open(self.password_path, "w") as f:
            json.dump(self.passwords, f)
        self.refresh_password_list(self.passwords)

    def refresh_password_list(self, passwords):
        self.list_widget.clear()
        for login_pair in passwords:
            username = login_pair["username"]
            item = QListWidgetItem(username)
            self.list_widget.addItem(item)

    def check_password_strength(self, password, min_len, has_num, has_special_chars):
        # Kontrola minimální délky
        if len(password) < min_len:
            return False

        # Kontrola, zda heslo obsahuje číslo
        if has_num and not any(char.isdigit() for char in password):
            return False

        # Kontrola, zda heslo obsahuje speciální znak
        special_characters = string.punctuation  # Všechny speciální znaky (!, @, #, atd.)
        if has_special_chars and not any(char in special_characters for char in password):
            return False

        return True


    def show_detail(self, item):
        username = item.text()  # Získáme uživatelské jméno z položky seznamu
        password = None  # Inicializujeme heslo jako None

        # Prohledáme seznam hesel ručně
        for entry in self.passwords:
            if entry["username"] == username:
                password = entry["password"]
                break  # Jakmile najdeme, ukončíme smyčku

        # Pokud heslo bylo nalezeno, zobrazíme detail
        if password is not None:
            self.detail_window = PasswordDetail(username, password)
            self.detail_window.show()
        else:
            # Možná chyba v datech, heslo nebylo nalezeno
            QMessageBox.warning(self, "Chyba", f"Heslo pro uživatele {username} nebylo nalezeno.")


class PasswordDetail(QWidget):
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Detail hesla")

        # Layout pro detail hesla
        layout = QVBoxLayout()

        # Uživatelské jméno
        username_label = QLabel(f"Uživatelské jméno: {self.username}")
        layout.addWidget(username_label)

        # Heslo
        password_label = QLabel(f"Heslo: {self.password}")
        layout.addWidget(password_label)

        # Zavírací tlačítko
        close_button = QPushButton("Zavřít")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        # Nastavení layoutu
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    window = PasswordManager()
    window.show()
    app.exec_()
