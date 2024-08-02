from clases.Persona import Persona

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
