# empleado.py
from classGerente import Gerente
from classPersona import Persona

class Empleado(Gerente, Persona):
    def __init__(self):
        Gerente.__init__(self)
        Persona.__init__(self)
        self._puesto = ""
        self._antiguedad = 0

    def set_puesto(self, puesto):
        self._puesto = puesto

    def get_puesto(self):
        return self._puesto

    def set_antiguedad(self, antiguedad):
        self._antiguedad = antiguedad

    def get_antiguedad(self):
        return self._antiguedad

