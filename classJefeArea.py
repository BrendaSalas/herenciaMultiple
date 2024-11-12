# jefe_area.py
from classArea import Area

class JefeArea(Area):
    def __init__(self):
        super().__init__()
        self._equipo = ""

    def set_equipo(self, equipo):
        self._equipo = equipo

    def get_equipo(self):
        return self._equipo

