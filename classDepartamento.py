# departamento.py
from classDirector import Director

class Departamento(Director):
    def __init__(self):
        super().__init__()
        self._area = ""

    def set_area(self, area):
        self._area = area

    def get_area(self):
        return self._area
