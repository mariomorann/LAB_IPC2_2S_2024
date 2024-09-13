from Nodo import Nodo

class ListaPizzas:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert(self, newValue):
        newNode = Nodo(newValue)
        if self.head is None:
            self.head = newNode
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = newNode
    
    def eliminar(self, newValue):
        newNode = Nodo(newValue)
        if self.head is None:
            self.head = newNode
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = newNode
    
    def getInfo(self):
        if self.head is not None:
            actual = self.head
            while actual.next is not None:
                print(actual.value, end="->")
                actual = actual.next
            print("None")
            


    
    