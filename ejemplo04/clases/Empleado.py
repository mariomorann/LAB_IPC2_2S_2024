from clases.Persona import Persona

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
