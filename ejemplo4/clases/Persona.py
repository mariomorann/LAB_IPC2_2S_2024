
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
