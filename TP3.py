import TDA_Colas
import TDA_Pilas
cola = TDA_Colas.TCola()
pila=TDA_Pilas.TPila()

##### CARGAR Y LISTAR ###

def cargarint(cola):
    while not TDA_Colas.ColaLlena(cola):
        print("ingrese un numero a la cola")
        numero = int(input())
        #numero = random.randint(1,100)
        TDA_Colas.Encolar(cola,numero)

def cargarstr(cola):
    print("ingrese una palabra a la cola")
    palabra = input()
    for i in range (0,len(palabra)):
        TDA_Colas.Encolar(cola, palabra[i])

def cargarintp(pila):
    while not (TDA_Pilas.PilaLlena(pila)):
        print("ingrese un numero a la pila")
        numero = int(input())
        #numero = random.randint(1,100)
        TDA_Pilas.Apilar(pila, numero)

def cargarstrp(pila):
    print("ingrese una palabra a la pila")
    palabra = input()
    for i in range(0,len(palabra)):
        TDA_Pilas.Apilar(pila, palabra)
        
def listarc(cola):
  ##  colaaux = TDA_Colas.TCola()
  ##  colaaux = cola
    while not (TDA_Colas.ColaVacia(cola)):
        print(TDA_Colas.Desencolar(cola))
  ##  cola = colaaux
  
def listarp(pila):
    while (not TDA_Pilas.PilaVacia(pila)):
        print(TDA_Pilas.Desapilar(pila))  

### EJERCICIOS ###

def ejercicio3(cola):
    cargarint(cola)
    pilaaux = TDA_Pilas.TPila()
    while not (TDA_Colas.ColaVacia(cola)):
        x = TDA_Colas.Desencolar(cola)
        TDA_Pilas.Apilar(pilaaux,x)
    listarp(pilaaux)    

def ejercicio4(cola,pila):
    aux=0
    print("ingrese una palabra")
    palabra = input()
    for i in range (0,len(palabra)):
        TDA_Colas.Encolar(cola, palabra[i])
        TDA_Pilas.Apilar(pila, palabra[i])    
    while not (TDA_Pilas.PilaVacia(pila)):
        a=TDA_Pilas.Desapilar(pila)
        b=TDA_Colas.Desencolar(cola)
        if (a==b):
            aux=aux+1
    if(aux==len(palabra)):
        print("es un palindromo")
    else:
        print("no es un palindromo")
        
def ejercicio5(cola,pila):
    pilaaux=TDA_Pilas.TPila()
    colaaux=TDA_Colas.TCola()   
    print("Elija una opcion")
    print("A- Mover elementos de una pila a una cola")
    print("B- Mover elementos de una cola a una pila")
    print("C- Vaciar una pila en otra pila, manteniendo el mismo orden")
    print("D- Vaciar una pila en otra pila, con el orden invertido")
    print("E- Usar una pila vacia para invertir el orden de una cola")
    print("F- Usar una cola vacia para invertir el orden de una pila")
    letra=input()
    if (letra=="a"):
        cargarintp(pila)
        while not (TDA_Pilas.PilaVacia(pila)):
            x=TDA_Pilas.Desapilar(pila)
            TDA_Colas.Encolar(colaaux,x)
            listarc(colaaux)
    if (letra=="b"): 
        cargarint(cola)
        while not (TDA_Colas.ColaVacia(cola)):
            y=TDA_Colas.Desencolar(cola)
            TDA_Pilas.Apilar(pilaaux,y)
            listarp(pilaaux)
    if (letra=="c"):
        pilaaux2=TDA_Pilas.TPila()
        cargarintp(pila)
        while not (TDA_Pilas.PilaVacia(pila)):
            x=TDA_Pilas.Desapilar(pila)
            TDA_Pilas.Apilar(pilaaux,x)
        while not (TDA_Pilas.PilaVacia(pilaaux)):
            y=TDA_Pilas.Desapilar(pilaaux)
            TDA_Pilas.Apilar(pilaaux2,y)
        listarp(pilaaux2) 
    if (letra=="d"):
        cargarintp(pila)
        while not (TDA_Pilas.PilaVacia(pila)):
            x=TDA_Pilas.Desapilar(pila)
            TDA_Pilas.Apilar(pilaaux,x)
        listarp(pilaaux) 
    if (letra=="e"):
        cargarint(cola)
        while not (TDA_Colas.ColaVacia(cola)):
            y=TDA_Colas.Desencolar(cola)
            TDA_Pilas.Apilar(pilaaux,y)
        while not (TDA_Pilas.PilaVacia(pilaaux)):
            x=TDA_Pilas.Desapilar(pilaaux)
            TDA_Colas.Encolar(cola,x)
        listarc(cola)
    if (letra=="f"):
        cargarintp(pila)
        while not (TDA_Pilas.PilaVacia(pila)):
            x=TDA_Pilas.Desapilar(pila)
            TDA_Colas.Encolar(colaaux,x)
        while not (TDA_Colas.ColaVacia(colaaux)):
            y=TDA_Colas.Desencolar(colaaux)
            TDA_Pilas.Apilar(pila,y)
        listarp(pila)    

def ejercicio6():
    colaizq=TDA_Colas.TCola()
    colader=TDA_Colas.TCola()
    palabra = input("ingrese una palabra a la cola ")
    aux=0
    for k in range (0,len(palabra)):
        if (palabra[k]==":"):
            aux=k
    if (aux!=0):        
        for i in range (0,aux):
            TDA_Colas.Encolar(colaizq,palabra[i])
        for j in range (aux+1,len(palabra)):
            TDA_Colas.Encolar(colader,palabra[j])    
    if (aux==0):
        print("No se encontraron dos puntos")
    izq=TDA_Colas.tamanio(colaizq)
    der=TDA_Colas.tamanio(colader)    
    if (izq>der):
        print("La parte izquierda es mayor")
    if (izq<der):
        print("La parte derecha es mayor")    
    if (izq==der):
        c=0
        while not (TDA_Colas.ColaVacia(colaizq)):
            a=TDA_Colas.Desencolar(colaizq)
            b=TDA_Colas.Desencolar(colader)
            print(a,b)
            if (a==b):
                c=c+1 
        if (c==izq):        
            print("Las partes tienen la misma longitud y son iguales")
        else:
            print("Las partes tienen la misma longitud pero son distintas")
        
#listarc(cola)
#ejercicio3(cola)
#ejercicio4(cola,pila)
#ejercicio5(cola,pila)
ejercicio6()