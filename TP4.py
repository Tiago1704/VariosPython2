from TDA_Listas import TLista,NodoLista,criterio,insertar,eliminar,tamanio,listavacia,mostrar
lista=TLista()
nodo=NodoLista()

def cargarlista(lista):
    print("Para agregar un elemento a la lista presione S")
    aux = input()
    while (aux=='s'):
        dato = input("ingrese un elemento a la lista")
        insertar(lista, dato)
        aux = input("Para agregar otro elemento a la lista presione S")
        