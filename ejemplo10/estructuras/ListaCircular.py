from estructuras.NodoCircular import Nodo
import graphviz
 
# Lista Circular

class ListaCircular:
    def __init__(self):
        self.inicio = None
    
    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.inicio is None:
            self.inicio = nuevo_nodo
            nuevo_nodo.siguiente = self.inicio
        else:
            actual = self.inicio
            while actual.siguiente != self.inicio:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.inicio
    
    def imprimir(self):
        actual = self.inicio
        while actual.siguiente != self.inicio:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print(actual.valor, end=" -> ")
        print("")

    def graficar(self):
        dot = graphviz.Graph(filename="archivo")
        dot.attr("node", shape="square")
        dot.attr(rankdir="LR")
        dot.edge_attr.update(arrowhead="vee")

        actual = self.inicio
        while True:
            dot.node(str(actual.valor), str(actual.valor))
            if actual.siguiente.valor is not None:
                dot.edge(str(actual.valor), str(actual.siguiente.valor), arrowhead="vee")
            actual = actual.siguiente
            if actual is self.inicio:
                break

        dot.render(directory="", view=True)
