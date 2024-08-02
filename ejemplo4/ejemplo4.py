from clases.Cliente import Cliente
from clases.Empleado import Empleado

def main():
    cliente1 = Cliente("Mario", 22, 202015123, 1)
    cliente1.getInfo()
    print("")
    empleado1 = Empleado("Pablo", 23, 201845612, 2)
    empleado1.getInfo()

if __name__ == "__main__":
    main()