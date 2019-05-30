from Clase_semaforo import Semaforo, TCola, Encolar, Desencolar, ColaVacia
import sys
from PyQt5.QtTest import QTest

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi

cola = TCola()
"""
def CargarSemaforos(cola):
    for i in range (0,4):
        y = i
        x = "rojo"
        Encolar(cola,y,x)
"""        
class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ventanasemaforo.ui", self)
        self.show()
      ##  CargarSemaforos(cola)
        for i in range (0,4):
            if (i=="1"):
                x = Desencolar(cola)
                x = "Amarillo"
                pixmap = QPixmap('SemaforoA.png')
                self.sem1.setPixmap(pixmap)
                QTest.qWait(5000)
                x = "Verde"
                pixmap = QPixmap('SemaforoV.png')
                self.sem1.setPixmap(pixmap)
                QTest.qWait(30000)
                x = "Rojo"
                Encolar(cola,i,x)
                pixmap = QPixmap('SemaforoR.png')
                self.sem1.setPixmap(pixmap)
            if (i=="2"):    
                x = Desencolar(cola)
                x = "Amarillo"
                pixmap2 = QPixmap('SemaforoA.png')
                self.sem2.setPixmap(pixmap2)
                QTest.qWait(5000)
                x = "Verde"
                pixmap2 = QPixmap('SemaforoV.png')
                self.sem2.setPixmap(pixmap2)
                QTest.qWait(30000)
                x = "Rojo"
                Encolar(cola,i,x)
                pixmap2 = QPixmap('SemaforoR.png')
                self.sem2.setPixmap(pixmap)
            if (i=="3"):
                x = Desencolar(cola)
                x = "Amarillo"
                pixmap3 = QPixmap('SemaforoA.png')
                self.sem3.setPixmap(pixmap3)
                QTest.qWait(5000)
                x = "Verde"
                pixmap3 = QPixmap('SemaforoV.png')
                self.sem3.setPixmap(pixmap3)
                QTest.qWait(30000)
                x = "Rojo"
                Encolar(cola,i,x)
                pixmap3 = QPixmap('SemaforoR.png')
                self.sem3.setPixmap(pixmap3)
            if (i=="4"):
                x = Desencolar(cola)
                x = "Amarillo"
                pixmap4 = QPixmap('SemaforoA.png')
                self.sem4.setPixmap(pixmap4)
                QTest.qWait(5000)
                x = "Verde"
                pixmap4 = QPixmap('SemaforoV.png')
                self.sem4.setPixmap(pixmap4)
                QTest.qWait(30000)
                x = "Rojo"
                Encolar(cola,i,x)
                pixmap4 = QPixmap('SemaforoR.png')
                self.sem4.setPixmap(pixmap4)
     ##   self.empezar.clicked.connect(self.CambiarColor)
"""
def CambiarColor(cola,self):
    for i in range (0,4):
        x = Desencolar(cola)
        x = "Amarillo"
        pixmap = QPixmap('SemaforoA.png')
        self.sem1.setPixmap(pixmap)
        QTest.qWait(5000)
        x = "Verde"
        pixmap = QPixmap('SemaforoV.png')
        self.sem1.setPixmap(pixmap)
        QTest.qWait(30000)
        x = "Rojo"
        pixmap = QPixmap('SemaforoR.png')
        self.sem1.setPixmap(pixmap)
        QTest.qWait(1000)
        Encolar(cola,i,x)

CargarSemaforos(cola)
        while (not ColaVacia(cola)):
            CambiarColor(cola)
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Principal()
    sys.exit(app.exec_())    