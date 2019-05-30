
#import random
from TDA_Pilas_Nodos import TPila, NodoPila, Apilar, Desapilar, PilaLlena, PilaVacia, Tamanio 


pila = TPila()
nodo = NodoPila()

def cargarint(pila):
    print("¿Cuantos numeros desea agregar a la pila?")
    aux = int(input())
    for i in range (0,aux):
        print("ingrese un numero a la pila")
        numero = int(input())
        #numero = random.randint(1,100)
        Apilar(pila, numero)

def cargarstr(pila):
    print("ingrese una palabra a la pila")
    palabra = input()
    for i in range(0,len(palabra)):
        Apilar(pila, palabra[i])

def listar(pila):
    while (not PilaVacia(pila)):
        print(Desapilar(pila))
    
def ejercicio1(pila):
    print("Ingrese el elemento que desea buscar en la pila")
    x = int(input())
    cont = 0
    while not (PilaVacia(pila)):
        aux = Desapilar(pila)
        if (aux == x):
            cont = cont+1
    return print("El elemento ",x," se repite ",cont," veces")

def ejercicio2(pila):    
    pilaaux = TPila()
    while not (PilaVacia(pila)):
        aux = Desapilar(pila)
        if (aux % 2 == 0):
            Apilar(pilaaux,aux)
    print("  ")        
    print("los elementos de la pila auxiliar son") 
    listar(pilaaux)           
    
def ejercicio3(pila):    
    pilaaux = TPila()
    print("Ingrese el elemento de la pila que desea modificar")
    aux = int(input())
    print("ingrese el nuevo elemento de la pila que desea modificar")
    mod = int(input())
    while not (PilaVacia(pila)):
        num = Desapilar(pila)
        if (num == aux):
            Apilar(pilaaux,mod)
        else: 
            Apilar(pilaaux,num)
    while not (PilaVacia(pilaaux)):
        x = Desapilar(pilaaux)
        Apilar(pila,x)
    print("   ")
    print("La nueva pila modificada es")
    listar(pila)
    
def ejercicio4(pila):
    pilaaux = TPila()
    while not (PilaVacia(pila)):
        aux = Desapilar(pila)
        Apilar(pilaaux,aux)
    print("   ")
    print("La pila invertida es")
    listar(pilaaux)    
        
def ejercicio5(pila):##preguntar a walter
    print("ingrese una palabra a la pila")
    palabra = input()
    for i in range(0,len(palabra)):
        Apilar(pila, palabra)    
    pilaaux1 = TPila()   
    pilaaux2 = pila
    z=0
    while not (PilaVacia(pila)):
        aux = Desapilar(pila)
        Apilar(pilaaux1,aux)
    while not (PilaVacia(pilaaux1)):
        a=Desapilar(pilaaux1)
        b=Desapilar(pilaaux2)
        if (a==b):
            z=z+1
    if (z==len(palabra)):        
        print("La palabra es un palindromo")
    else:
        print("La palabra no es un palindromo")

def ejercicio6():
    pilaaux=TPila()
    c=0
    palabra = input("ingrese una palabra a la cola ")
    aux=0
    for k in range (0,len(palabra)):
        Apilar(pila, palabra[k])
        if (palabra[k]=="c"):
            aux=k
    for i in range (aux+1,len(palabra)):
        x=Desapilar(pila)
        Apilar(pilaaux,x)
    Desapilar(pila)
    k=Tamanio(pila)
    while not (PilaVacia(pilaaux)):
        a=Desapilar(pila)
        b=Desapilar(pilaaux)
        if (a==b):
            c=c+1      
    if (k==c):
        print("La palabra xCy es inversa")
    else:
        print("No es inversa")
    
def ejercicio7(pila):
    pilaaux = TPila()
    while not (PilaVacia(pila)):
        aux = Desapilar(pila)
        Apilar(pilaaux,aux)
    print("   ")
    print("La palabra invertida es")
    listar(pilaaux)     

def ejercicio8(pila):
    aux = Desapilar(pila)
    Desapilar(pila)
    Apilar(pila,aux)
    print("   ")
    print("La pila sin el elemento debajo de la cima es")
    listar(pila)
    
def ejercicio9(pila):
    pilaaux = TPila()
    aux = int(input("¿Que elemento iesimo de la pila desea obtener?"))
    tam = Tamanio(pila)
    if (aux<=tam):
        while (aux!=Tamanio(pila)):
            x = Desapilar(pila)
            Apilar(pilaaux,x)
        k = Desapilar(pila)
        print("el elemento en la posicion ",aux," de la pila es: ",k)
        Apilar(pilaaux,k)
        while not (PilaVacia(pilaaux)):
            y = Desapilar(pilaaux)
            Apilar(pila,y)
    else:
        print("el elemento iesimo pedido es mayor que el tamaño de la pila")        
        
cargarint(pila)
#cargarstr(pila)
listar(pila)
#ejercicio1(pila)
#ejercicio2(pila)
#ejercicio3(pila) 
#ejercicio5(pila)  
#ejercicio6()
#ejercicio7(pila)
#ejercicio8(pila)
#ejercicio9(pila)