
import random
def listaAleatorios(n):
      for i in range(n):
          lista[i] = random.randrange(0,n)
      return lista

def listarLista(n):
    for i in range (n):
        print (lista[i])

def Quicksort(lista,inf,sup):
    if (inf<sup):
        I=inf
        J=sup
        pivot=lista[inf]
        while (I<J):
            while (lista[I]<=pivot) and (I<J):
                I+=1
            while (lista[J]>pivot):
                J-=1
            if (I<J):
                (lista[I],lista[J])=(lista[J],lista[I])
        (lista[inf],lista[J])=(lista[J],lista[inf])
        Quicksort(lista,inf,J-1)
        Quicksort(lista,J+1,sup)

def bb(Pri,Ult,lista,Kx):
    if (Pri<=Ult):
        M=(Pri+Ult)//2    
        if (lista[M]==Kx):
            return M
        else:
            if (lista[M]>Kx):                               
                return bb(Pri,M-1,lista,Kx)
            elif (lista[M]<Kx):
                return bb(M+1,Ult,lista,Kx)

n=10
lista = [0]  * n
listaAleatorios(n)
print("la lista random es:")
listarLista(n)
print(" ")
Quicksort(lista,0,len(lista)-1)
print("la lista random ordenada es:")
listarLista(n)
print(" ")
print("ingrese el numero que desea buscar en la lista")
bus= int(input())
pos=bb(0,len(lista),lista,bus)
print("el numero ",bus," se encuentra en la posicion ",pos+1) 