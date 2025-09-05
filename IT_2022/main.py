# app.py
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Input Display")
        self.layout = QVBoxLayout()

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter text here...")
        self.layout.addWidget(self.input_field)

        self.display_label = QLabel("")
        self.layout.addWidget(self.display_label)

        self.show_button = QPushButton("Show Text")
        self.show_button.clicked.connect(self.show_text)
        self.layout.addWidget(self.show_button)

        self.setLayout(self.layout)

    def show_text(self):
        text = self.input_field.text()
        self.display_label.setText(text)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
