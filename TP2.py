
#import random
import TDA_Pilas

pila = TDA_Pilas.TPila()

def cargarint(pila):
    while not (TDA_Pilas.PilaLlena(pila)):
        print("ingrese un numero a la pila")
        numero = int(input())
        #numero = random.randint(1,100)
        TDA_Pilas.Apilar(pila, numero)

def cargarstr(pila):
    print("ingrese una palabra a la pila")
    palabra = input()
    for i in range(0,len(palabra)):
        TDA_Pilas.Apilar(pila, palabra[i])

def listar(pila):
    while (not TDA_Pilas.PilaVacia(pila)):
        print(TDA_Pilas.Desapilar(pila))
    
def ejercicio1(pila):
    print("Ingrese el elemento que desea buscar en la pila")
    x = int(input())
    cont = 0
    while not (TDA_Pilas.PilaVacia(pila)):
        aux = TDA_Pilas.Desapilar(pila)
        if (aux == x):
            cont = cont+1
    return print("El elemento ",x," se repite ",cont," veces")

def ejercicio2(pila):    
    pilaaux = TDA_Pilas.TPila()
    while not (TDA_Pilas.PilaVacia(pila)):
        aux = TDA_Pilas.Desapilar(pila)
        if (aux % 2 == 0):
            TDA_Pilas.Apilar(pilaaux,aux)
    print("  ")        
    print("los elementos de la pila auxiliar son") 
    listar(pilaaux)           
    
def ejercicio3(pila):    
    pilaaux = TDA_Pilas.TPila()
    print("Ingrese el elemento de la pila que desea modificar")
    aux = int(input())
    print("ingrese el nuevo elemento de la pila que desea modificar")
    mod = int(input())
    while not (TDA_Pilas.PilaVacia(pila)):
        num = TDA_Pilas.Desapilar(pila)
        if (num == aux):
            TDA_Pilas.Apilar(pilaaux,mod)
        else: 
            TDA_Pilas.Apilar(pilaaux,num)
    while not (TDA_Pilas.PilaVacia(pilaaux)):
        x = TDA_Pilas.Desapilar(pilaaux)
        TDA_Pilas.Apilar(pila,x)
    print("   ")
    print("La nueva pila modificada es")
    listar(pila)
    
def ejercicio4(pila):
    pilaaux = TDA_Pilas.TPila()
    while not (TDA_Pilas.PilaVacia(pila)):
        aux = TDA_Pilas.Desapilar(pila)
        TDA_Pilas.Apilar(pilaaux,aux)
    print("   ")
    print("La pila invertida es")
    listar(pilaaux)    
        
def ejercicio5(pila):##preguntar a walter
    print("ingrese una palabra a la pila")
    palabra = input()
    for i in range(0,len(palabra)):
        TDA_Pilas.Apilar(pila, palabra)    
    pilaaux1 = TDA_Pilas.TPila()   
    pilaaux2 = pila
    z=0
    while not (TDA_Pilas.PilaVacia(pila)):
        aux = TDA_Pilas.Desapilar(pila)
        TDA_Pilas.Apilar(pilaaux1,aux)
    while not (TDA_Pilas.PilaVacia(pilaaux1)):
        a=TDA_Pilas.Desapilar(pilaaux1)
        b=TDA_Pilas.Desapilar(pilaaux2)
        if (a==b):
            z=z+1
    if (z==len(palabra)):        
        print("La palabra es un palindromo")
    else:
        print("La palabra no es un palindromo")

def ejercicio6():
    pilaaux=TDA_Pilas.TPila()
    c=0
    palabra = input("ingrese una palabra a la cola ")
    aux=0
    for k in range (0,len(palabra)):
        TDA_Pilas.Apilar(pila, palabra[k])
        if (palabra[k]=="c"):
            aux=k
    for i in range (aux+1,len(palabra)):
        x=TDA_Pilas.Desapilar(pila)
        TDA_Pilas.Apilar(pilaaux,x)
    TDA_Pilas.Desapilar(pila)
    k=TDA_Pilas.tamanio(pila)
    while not (TDA_Pilas.PilaVacia(pilaaux)):
        a=TDA_Pilas.Desapilar(pila)
        b=TDA_Pilas.Desapilar(pilaaux)
        if (a==b):
            c=c+1      
    if (k==c):
        print("La palabra xCy es inversa")
    else:
        print("No es inversa")
    
def ejercicio7(pila):
    pilaaux = TDA_Pilas.TPila()
    while not (TDA_Pilas.PilaVacia(pila)):
        aux = TDA_Pilas.Desapilar(pila)
        TDA_Pilas.Apilar(pilaaux,aux)
    print("   ")
    print("La palabra invertida es")
    listar(pilaaux)     

def ejercicio8(pila):
    aux = TDA_Pilas.Desapilar(pila)
    TDA_Pilas.Desapilar(pila)
    TDA_Pilas.Apilar(pila,aux)
    print("   ")
    print("La pila sin el elemento debajo de la cima es")
    listar(pila)
    
def ejercicio9(pila):
    pilaaux = TDA_Pilas.TPila()
    aux = int(input("¿Que elemento iesimo de la pila desea obtener?"))
    tam = TDA_Pilas.tamanio(pila)
    if (aux<=tam):
        while (aux!=TDA_Pilas.tamanio(pila)):
            x = TDA_Pilas.Desapilar(pila)
            TDA_Pilas.Apilar(pilaaux,x)
        k = TDA_Pilas.Desapilar(pila)
        print("el elemento en la posicion ",aux," de la pila es: ",k)
        TDA_Pilas.Apilar(pilaaux,k)
        while not (TDA_Pilas.PilaVacia(pilaaux)):
            y = TDA_Pilas.Desapilar(pilaaux)
            TDA_Pilas.Apilar(pila,y)
    else:
        print("el elemento iesimo pedido es mayor que el tamaño de la pila")        
        
#cargarint(pila)
#cargarstr(pila)
#ejercicio1(pila)
#ejercicio2(pila)
#ejercicio3(pila) 
#ejercicio5(pila)  
ejercicio6()
#ejercicio7(pila)
#ejercicio8(pila)
#ejercicio9(pila)