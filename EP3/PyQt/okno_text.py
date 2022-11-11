from PyQt5 import QtWidgets

app = QtWidgets.QApplication([]) # inicializace aplikace

hlavni_okno = QtWidgets.QWidget()  # vytvoření objektu hlavního okna
hlavni_okno.setWindowTitle("Můj supr program")  # název okna

usporadani = QtWidgets.QVBoxLayout() # vytvoření layoutu
hlavni_okno.setLayout(usporadani) # aplikace layoutu na hlavni_okno

napis = QtWidgets.QLabel("Nějaký text...") # vytvoření objektu napis
usporadani.addWidget(napis) # "nalepení" textu na hlavni_okno

napis = QtWidgets.QLabel("Nějaký další text...") # vytvoření objektu napis
usporadani.addWidget(napis) # "nalepení" textu na hlavni_okno

tlacitko = QtWidgets.QPushButton("Klikni na mě...")
usporadani.addWidget(tlacitko)

hlavni_okno.show() # okno bude viditelné

app.exec() # spuštění aplikace