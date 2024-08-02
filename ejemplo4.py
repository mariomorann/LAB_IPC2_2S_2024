class Persona:
    # atributos
    _nombre = ""
    _edad = 0
    _carnet = 0  
    # constructor
    def __init__(self, nombre, edad, carnet):
        self._nombre = nombre
        self._edad = edad
        self._carnet = carnet
    # getters / setters
    def getCarnet(self):
        return self._carnet
    def setCarnet(self, carnet):
        self._carnet = carnet
    
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getEdad(self):
        return self._edad
    def setEdad(self, edad):
        self._edad = edad
    # métodos
    def getInfo(self):
        print(self.getCarnet(), "-", self.getNombre(), "-", self.getEdad())

# Herencia
class Cliente(Persona):
    # atributos
    _codigoCliente = 0
    # constructor
    def __init__(self, nombre, edad, carnet, codigoCliente):
        # asignacion atributos del padre
        super().__init__(nombre, edad, carnet)
        # asignacion atributos del Cliente
        self._codigoCliente = codigoCliente
    # métodos
    def getInfo(self):
        print("Cliente: ",self.getCarnet(),"-",self.getNombre(),"-",self.getEdad(),"-",self._codigoCliente)

class Empleado(Persona):
    # atributos
    _codigoEmpleado = 0
    # constructor
    def __init__(self, nombre, edad, carnet, codigoEmpleado):
        super().__init__(nombre, edad, carnet)
        self._codigoEmpleado = codigoEmpleado
    # métodos
    def getInfo(self):
        print("Empleado: ",self.getCarnet(),"-",self.getNombre(),"-",self.getEdad(),"-",self._codigoEmpleado)

def main():
    cliente1 = Cliente("Mario", 22, 202015123, 1)
    cliente1.getInfo()
    print("")
    empleado1 = Empleado("Pablo", 23, 201845612, 2)
    empleado1.getInfo()

if __name__ == "__main__":
    main()