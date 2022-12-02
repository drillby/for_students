from PyQt5 import QtWidgets

app = QtWidgets.QApplication([]) # inicializace aplikace

hlavni_okno = QtWidgets.QWidget()  # vytvoření objektu hlavního okna
hlavni_okno.setWindowTitle("Můj supr program")  # název okna

usporadani = QtWidgets.QGridLayout() # vytvoření grid layoutu
# vytvoření layoutu
hlavni_okno.setLayout(usporadani) # aplikace layoutu na hlavni_okno

"""tlacitko = QtWidgets.QPushButton("Loakce (0, 0)")
usporadani.addWidget(tlacitko, 0, 0)

usporadani.addWidget(QtWidgets.QPushButton("Loakce (0, 1)"), 0, 1)
usporadani.addWidget(QtWidgets.QPushButton("Loakce (0, 2)"), 0, 2)
usporadani.addWidget(QtWidgets.QPushButton("Loakce (1, 0)"), 1, 0)
usporadani.addWidget(QtWidgets.QPushButton("Loakce (1, 1)"), 1, 1)
usporadani.addWidget(QtWidgets.QPushButton("Loakce (1, 2)"), 1, 2)
usporadani.addWidget(QtWidgets.QPushButton("Loakce (2, 1)"), 2, 1)
usporadani.addWidget(QtWidgets.QPushButton("Loakce (2, 2)"), 2, 2)
usporadani.addWidget(QtWidgets.QPushButton("Loakce (2, 0)"), 2, 0)"""

pocet_tlacitek_x = 5
pocet_tlacitek_y = 3

for souradnice_x in range(pocet_tlacitek_x): # cyklus pro dosazení tlačítek na ose x
    for souradnice_y in range(pocet_tlacitek_y): # cyklus pro dosazení tlačítek na ose y
        usporadani.addWidget(
            QtWidgets.QPushButton(
                f"Loakce ({souradnice_x}, {souradnice_y})"
            ), souradnice_x, souradnice_y) # vytvoření tlačítka a dosazení na lokaci podle chodu cyklů

hlavni_okno.show() # okno bude viditelné

app.exec_() # spuštění aplikace