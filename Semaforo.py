from TDA_Colas_Nodos import TCola, Encolar, Desencolar, ColaLlena, ColaVacia, Tamanio 
from PyQt5.QtTest import QTest
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi

class Semaforo():#se crea la clase semaforo
    def __init__(self, id, color, tiempo):
        self.id = id
        self.color= color
        self.tiempo= tiempo

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ventanasemaforo.ui", self)
        self.show()
        self.cola = TCola() #crea la cola
        self.crear_sem()#llama la funcion crear semaforos

    def crear_sem (self):
        Sem1=Semaforo("1","rojo",10000)#crea los 4 objetos semaforos (son registros con los campos: id, color, tiempo)
        Sem2=Semaforo("2","rojo",10000)
        Sem3=Semaforo("3","rojo",10000)
        Sem4=Semaforo("4","rojo",10000)
        
        pixmap = QPixmap('SemaforoR.png')#crea los 4 semaforos de la interfaz y les asigna la foto del rojo
        self.sem1.setPixmap(pixmap)
        self.sem2.setPixmap(pixmap)
        self.sem3.setPixmap(pixmap)
        self.sem4.setPixmap(pixmap)
    
        Encolar(self.cola,Sem1)#encola los 4 semaforos a la cola
        Encolar(self.cola,Sem2)
        Encolar(self.cola,Sem3)
        Encolar(self.cola,Sem4)
        
        while (not(ColaVacia(self.cola))):#hace que el ciclo de cambiar color se ejecute infinitamente
            self.CambiarColor(self.cola)#llama a la funcion cambiar color
    
    def CambiarColor(self,cola):#funcion cambiar color
        for i in range (0,4):#un ciclo for de 0 a 4 para que desencole los 4 semaforos
            x = Desencolar(cola)
            #determinar semaforo
            semaforo = None#es una variable que se reutiliza para manejar el semaforo de la interfaz
            if(x.id=="1"):#se pregunta que id es el semaforo que se desencolo
                semaforo = self.sem1#se le asigna a esa variable reutilizada el semaforo de la interfaz
                x.color = "Amarillo"#se cambia de color el campo color del semaforo
                pixmap = QPixmap('SemaforoA.png')#se carga la foto del semaforo en amarillo
                semaforo.setPixmap(pixmap)#se muestra la foto del semaforo en amarillo
                QTest.qWait(5000)#se le dice que muestre el semaforo amarillo por 5 seg
                x.color = "Verde"#se cambia de color el campo color del semaforo
                pixmap = QPixmap('SemaforoV.png')#se carga la foto del semaforo en verde
                semaforo.setPixmap(pixmap)#se muestra la foto del semaforo en verde
                QTest.qWait(x.tiempo)#se le dice que muestre el semaforo verde el tiempo que esta indicado en el campo tiempo del semaforo
                x.color = "Rojo"#se cambia de color el campo color del semaforo
                pixmap = QPixmap('SemaforoR.png')#se carga la foto del semaforo en rojo
                semaforo.setPixmap(pixmap)#se muestra la foto del semaforo en rojo
            if(x.id=="2"):
                semaforo = self.sem2
                x.color = "Amarillo"
                pixmap = QPixmap('SemaforoA.png')
                semaforo.setPixmap(pixmap)
                QTest.qWait(5000)
                x.color = "Verde"
                pixmap = QPixmap('SemaforoV.png')
                semaforo.setPixmap(pixmap)
                QTest.qWait(x.tiempo)
                x.color = "Rojo"
                pixmap = QPixmap('SemaforoR.png')
                semaforo.setPixmap(pixmap)
            if(x.id=="3"):
                semaforo = self.sem3
                x.color = "Amarillo"
                pixmap = QPixmap('SemaforoA.png')
                semaforo.setPixmap(pixmap)
                QTest.qWait(5000)
                x.color = "Verde"
                pixmap = QPixmap('SemaforoV.png')
                semaforo.setPixmap(pixmap)
                QTest.qWait(x.tiempo)
                x.color = "Rojo"
                pixmap = QPixmap('SemaforoR.png')
                semaforo.setPixmap(pixmap)
            if(x.id=="4"):
                semaforo = self.sem4
                x.color = "Amarillo"
                pixmap = QPixmap('SemaforoA.png')
                semaforo.setPixmap(pixmap)
                QTest.qWait(5000)
                x.color = "Verde"
                pixmap = QPixmap('SemaforoV.png')
                semaforo.setPixmap(pixmap)
                QTest.qWait(x.tiempo)
                x.color = "Rojo"
                pixmap = QPixmap('SemaforoR.png')
                semaforo.setPixmap(pixmap)
            Encolar(cola,x)#se vuelve a encolar el semaforo desencolado y continua ejecutandose el for con los otros semaforos que faltan

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Principal()
    sys.exit(app.exec_())   