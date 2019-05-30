from TDA_Pilas import TPila, Apilar, Desapilar, PilaVacia,PilaLlena
import random
pila=TPila()

def QuicksortI(pila,izq,der):
    Apilar(pila,izq)
    Apilar(pila,der)
    while (not PilaVacia):
        der = Desapilar(pila)
        izq = Desapilar(pila)
        while (izq>=der):
            pivot = pila[(izq+der)/2]
            i = izq
            d = der
            while (i>=d):
                while (pila[i]<pivot):
                    i = i+1
                while (pila[d]>pivot):
                    d = d-1
                if (i<=d):
                    if (i!=d):
                        (pila[i],pila[d])=(pila[d],pila[i])
                    i=i+1
                    d=d-1
            if (i-izq>der-d):
                if (izq<d):
                    Apilar(pila,izq)
                    Apilar(pila,d)
                izq=i
            else:
                if (i<der):
                    Apilar(pila,i)
                    Apilar(pila,der)
                der=d    

def listar(pila):
    while (not PilaVacia(pila)):
        print(Desapilar(pila))

def cargarint(pila):
    while not (PilaLlena(pila)):
        numero = random.randint(1,100)
        Apilar(pila, numero)

cargarint(pila)    
QuicksortI(pila,0,10)
listar(pila)
"""
function QuickSort(Array, Left, Right)
 var
     L2, R2, PivotValue
 begin
     Stack.Push(Left, Right);       // pushes Left, and then Right, on to a stack
     while not Stack.Empty do
     begin
         Stack.Pop(Left, Right);    // pops 2 values, storing them in Right and then Left
         repeat
             PivotValue := Array[(Left + Right) div 2];
             L2 := Left;
             R2 := Right;
             repeat
                 while Array[L2] < PivotValue do // scan left partition
                     L2 := L2 + 1;
                 while Array[R2] > PivotValue do // scan right partition
                     R2 := R2 - 1;
                 if L2 <= R2 then
                 begin
                     if L2 != R2 then
                         Swap(Array[L2], Array[R2]);  // swaps the data at L2 and R2
                     L2 := L2 + 1;
                     R2 := R2 - 1;
                 end;
             until L2 >= R2;
             if R2 - Left > Right - L2 then // is left side piece larger?
             begin
                 if Left < R2 then
                     Stack.Push(Left, R2);
                 Left := L2;
             end;
             else
             begin
                 if L2 < Right then // if left side isn't, right side is larger
                     Stack.Push(L2, Right);
                 Right := R2;
             end;
         until Left >= Right;
     end;
 end;
"""