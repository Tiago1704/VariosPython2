import sys

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication

class Principal(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi("ventana.ui", self)
        self.show()
        
        self.enviar.clicked.connect(self.agregar_texto)
        
    def agregar_texto(self):
        self.texto.setText("Ok")
        self.enviar.setText("nuevo")
        
        #self.ver.clicked.connect(self.abrir_menu_m)
        #self.agregar_museo.clicked.connect(self.agregar_museo_)

"""
    def abrir_menu_m(self):
        if(self.tabla.currentRow() >= 0):
            menu_m = menu_muestra.Menu_Muestra(self.lista_museos[int(self.tabla.currentRow())])
            menu_m.exec_()

    def agregar_museo_(self):
        menu_cargam = cargar_museo.Cargar_Museo()
        menu_cargam.exec_()
        self.lista_museos.append(menu_cargam.museo)
        self.actualizar_tabla()

    def actualizar_tabla(self):
        self.tabla.setRowCount(0)
        for museo in self.lista_museos:
            self.tabla.insertRow(self.tabla.rowCount())
            self.tabla.setItem(self.tabla.rowCount()-1, 0,
                               QTableWidgetItem(str(museo.nombre)))
            self.tabla.setItem(self.tabla.rowCount()-1, 1,
                               QTableWidgetItem(museo.direccion))

"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Principal()
    sys.exit(app.exec_())