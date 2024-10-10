# Beispieldatei qt-hw.py
import sys
from PyQt6 import QtCore , QtWidgets
from PyQt6.QtWidgets import QMainWindow, QLabel, QWidget,QPushButton
from PyQt6.QtCore import QSize , Qt
class MyWindow(QMainWindow):
    def __init__(self):
        # Konstruktor von QMainWindow aufrufen
        super().__init__()
        # Fenstergröße und Titel einstellen
        self.setMinimumSize(QSize(300 , 100))
        self.setWindowTitle( 'Makroverteilung ')
        # # Title -Widget erzeugen und in Fenster einbetten
        # title = QLabel('Makroverteilung', self)
        # title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.setCentralWidget(title)
        # Button-WIdgets erzeugen und in Fenster einbetten
        b1 = QPushButton("Button 1", self)
        b1.move(50, 30)
        b1.resize(120, 25)
        b1.clicked.connect(self.clicked1)
        b2 = QPushButton("Button 2 (Quit)", self)
        b2.move(50,60)
        b2.resize(b2.sizeHint()) #opt. Größe
        b2.clicked.connect(self.clicked2)
        
    #Funtkionen zur Reaktion auf Button Klicks
    
    def clicked1(self):
        print("button 1 wurde geklickt")
        
    def clicked2(self):
        print("button 2 wurde geklickt. Programmende")
        app.quit()
# Fenster öffnen; das Programm läuft, bis das
# Fenster geschlossen wird
app = QtWidgets.QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec())

