from estructuras.NodoDoble import Nodo

# Lista Doblemente Enlazada

class ListaDoblementeEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None
    
    def agregar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.inicio is None:
            self.inicio = self.fin = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.fin
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo
        
    def agregar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.inicio is None:
            self.inicio = self.fin = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.inicio
            self.inicio.anterior = nuevo_nodo
            self.inicio = nuevo_nodo
        
    def imprimir(self):
        actual = self.inicio
        while actual:
            print(actual.valor, end= "-> ")
            actual = actual.siguiente
        print("")

    