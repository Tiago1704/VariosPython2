class NodoPila():
    def __init__(self):
        self.info = None
        self.sig= None
        
class TPila():
    def __init__(self):
        self.tamanio=0
        self.tope= None
        
def Apilar(Pila,x):
    aux= NodoPila()
    aux.info=x
    aux.sig=Pila.tope
    Pila.tope=aux
    Pila.tamanio+=1
    
def Desapilar(Pila):
    x=Pila.tope.info
    Pila.tope=Pila.tope.sig
    Pila.tamanio-=1
    return x

def Tamanio(Pila):
    return Pila.tamanio

def PilaVacia(Pila):
    return Pila.tope == None

def PilaLlena(Pila):
    return False



    