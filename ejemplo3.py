
class Persona:
    # atributos
    _nombre = ""
    _edad = 0
    _dpi = 0
    # contructor
    def __init__(self, nombre, edad, dpi):
        self._nombre = nombre
        self._edad = edad
        self._dpi = dpi
    # getters / setters
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getEdad(self):
        return self._edad
    
    def getDPI(self):
        return self._dpi
    # métodos
    def getInfo(self):
        print(self.getDPI(), " - ", self.getNombre(), " - ", self.getEdad())

# Herencia
class Cliente(Persona):
    _codigoCliente = 0
    # constructor
    def __init__(self, nombre, edad, dpi, codigoCliente):
        # asignación de atributos heredados
        super().__init__(nombre, edad, dpi)
        # asignación de atributos de Cliente
        self._codigoCliente = codigoCliente
    # getter
    def getCodigoCliente(self):
        return self._codigoCliente
    # métodos
    def getInfo(self):
        print(self.getDPI(), " - ", self.getNombre(), " - ", self.getEdad(), " - ", self._codigoCliente)

class Empleado(Persona):
    _codigoEmpleado = 0
    def __init__(self, nombre, edad, dpi, codigoEmpleado):
        super().__init__(nombre, edad, dpi)
        self._codigoEmpleado = codigoEmpleado
    # getter
    def getCodigoEmpleado(self):
        return self._codigoEmpleado
    # métodos
    def getInfo(self):
        print(self.getDPI(), " - ", self.getNombre(), " - ", self.getEdad(), " - ", self._codigoEmpleado)

def main():
    cliente = Cliente("Mario", 22, 1500, 1)
    cliente.getInfo()
    
    print("")

    empleado = Empleado("Cesar", 23, 2000, 2)
    empleado.getInfo()
    

if __name__ == "__main__":
    main()