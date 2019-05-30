max=5
class TCola():
    def __init__(self):
        self.frente=0
        self.final=-1
        self.tamanio=0
        self.dato=[]
        for I in range (0,max):
            self.dato.append(0)

#q=TCola()
'''
def CrearCola(q):
    q.frente=0
    q.final=0
    q.tamanio=0
'''

def Encolar(q,x):
    q.final=q.final+1
    q.tamanio=q.tamanio+1
    q.dato[q.final]=x
    
def Desencolar(q):
    x=q.dato[q.frente]
    q.frente=q.frente+1
    q.tamanio=q.tamanio-1
    return x
    
def ColaLlena(q):
    return q.tamanio == max

def ColaVacia(q):
    return q.tamanio == 0

def tamanio(q):
    return q.tamanio  
