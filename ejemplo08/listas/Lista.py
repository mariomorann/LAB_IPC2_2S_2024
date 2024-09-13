from listas.Nodo import Nodo


class Lista():
    def __init__(self):
        self.cabeza = None
        self.size = 0
    
    def insertar(self, valor):
        nuevoNodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevoNodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevoNodo
        self.size += 1
    
    def eliminar(self, nombre):
        actual = self.cabeza
        if actual is not None:
            if actual.valor.nombre == nombre:
                print("Pizza eliminada:", actual.valor.nombre)
                self.cabeza = actual.siguiente
                return
            else:
                while actual.siguiente is not None:
                    if (actual.siguiente.valor.nombre == nombre):
                        print("Pizza eliminada:", actual.siguiente.valor.nombre)
                        actual.siguiente = actual.siguiente.siguiente
                        return
                    actual = actual.siguiente
        else:
            print("No hay datos en la lista.")
    
    def getInfo(self):
        actual = self.cabeza
        if actual is not None:
            while actual is not None:
                print(actual.valor.nombre, actual.valor.precio)
                print(actual.valor.lista_ingredientes)
                print("")
                actual = actual.siguiente
        else:
            print("None")
