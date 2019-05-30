"""
ind: indice
val: valor
tel: telefono
ap: apellido
nom: nombre
"""
from TDA_Listas import TLista, insertar, busqueda,eliminar

class tda_hash():
    
    def __init__(self):
        self.u = [TLista()]
        self.d = []
        self.t = []
        self.db  = []
        self.tb = []
        for i in range(20, 99):
            self.d.append(TLista())

        for i in range(36, 88):
            self.t.append(TLista()) 
        
        for i in range(202, 983):
            self.db.append(TLista())
        
        for i in range(327, 894):
            self.tb.append(TLista())    

        self.guia = [self.u, self.d, self.t, self.db, self.tb]

    def f_hash(self, num):
        cont= num.tel.find('-') - 1
        aux = None
        if (cont < 3):
            ind = int (num.tel[0]) - 1
            lista = self.guia[ind]
            if(num.tel[0] == '1'):
                aux = lista[0]
            else:
                val = 20 if num.tel[0] == '2' else 36
                ind  = int(num.tel[1:3]) - val
                aux = lista[ind]
        else:
            ind = int(num.tel[0]) +1
            lista = self.guia[ind]
            val = 202 if num.tel[0]=='2' else 327
            ind  = int(num.tel[1:4]) - val
            aux = lista[ind]
        return aux
    
class Telefono():                                #Con esto lo usamos para crear la clase telefono jajajaj y no, no es un nokia
    def __init__(self, ap=None, nom=None, tel=None):
        self.ap = ap
        self.nom= nom
        self.tel = tel

def cargar_tel ():
        nume=Telefono()    
        print("Ingrese el apellido de la persona")
        nume.ap= input()
        print("Ingrese el nombre de la persona")
        nume.nom= input()
        print("Ingrese el numero telefonico de la persona (nnn-nnnnnn)")
        nume.tel= input()
        return nume

h = tda_hash()    #Acá ya empezamos con las tablas hash y su menú

def Menu(tabla_hash):
    control = True
    while control:
        print()
        print("1- Insertar un telefono en la guia")
        print("2- Eliminar un telefono en la guia")
        print("3- Buscar un telefono en la guia")
        print("4- salir")
        opc=input()
        if (opc=='1'):
            num = cargar_tel()
            puntero = tabla_hash.f_hash(num)
            aux = busqueda(puntero,num.tel,'telefono')
            if aux is None:
                insertar(puntero, num, 'apellido')
                print('se inserto con exito el telefono')
            else:
                print('ya existe')
        if (opc=='2'):
            aux=Telefono()
            print("Ingrese el numero telefonico de la persona (nnn-nnnnnn) que desea eliminar")
            aux.telefono= input()
            puntero = tabla_hash.f_hash(aux)
            x = busqueda(puntero,aux.telefono,'telefono')
            if x != None:
                eliminar(puntero,aux.telefono, 'telefono')
                print('se elimino con exito el telefono')
            else:
                print('no existe el telefono')
        if (opc=='3'):
            aux=Telefono()
            print('1- Buscar por telefono')
            print('2- Buscar por Apellido y Nombre')
            op=input()
            if op=='1':
                print("Ingrese el numero telefonico de la persona (nnn-nnnnnn) que desea buscar")
                aux.telefono= input()
                puntero = tabla_hash.f_hash(aux)
                x = busqueda(puntero,aux.telefono,'telefono')
                if x != None:
                    print('El apellido es: ',x.info.apellido)
                    print('El nombre es: ',x.info.nombre)
                    print('El telefono es: ',x.info.telefono)
                else:
                     print('no existe el telefono')
            if op=='2':
                print("Ingrese el apellido de la persona")
                aux.apellido= input()
                print("Ingrese el nombre de la persona")
                aux.nombre= input()
                for subguia in h.guia:
                    for ltel in subguia:
                        x = busqueda(ltel, aux.apellido, 'apellido')
                        if (x != None):
                            while (x != None and x.info.apellido==aux.apellido and x.info.nombre==aux.nombre):
                                print('El apellido es: ',x.info.apellido)
                                print('El nombre es: ',x.info.nombre)
                                print('El telefono es: ',x.info.telefono)
                                x = x.sig      
        if (opc=='4'):
            control = False

Menu(h) 
