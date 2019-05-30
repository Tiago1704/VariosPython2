class Semaforo():
    def __init__(self):
        self.id= None
        self.color= None
        self.sig= None
        
class TCola():
    def __init__(self):
        self.tamanio=0
        self.frente= None
        self.final= None
        
def Encolar(cola,y,x):
    aux = Semaforo
    aux.id = y
    aux.color = x
    aux.sig = None
    if (cola.final==None):
        cola.frente=aux
    else:
        cola.final.sig=aux
    cola.final=aux
    cola.tamanio=cola.tamanio+1
    
def Desencolar(cola):
    x = cola.frente.color
    aux = cola.frente
    cola.frente = aux.sig
    if (cola.frente==None):
        cola.final = None
    cola.tamanio = cola.tamanio-1
    return x

def Tamanio(cola):
    return cola.tamanio

def ColaLlena(cola):
    return False

def ColaVacia(cola):
    return cola.tamanio == 0