# gerente.py
from classArea import Area

class Gerente(Area):
    def __init__(self):
        super().__init__()
        self._departamento = ""

    def set_departamento(self, departamento):
        self._departamento = departamento

    def get_departamento(self):
        return self._departamento

