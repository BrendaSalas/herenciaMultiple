# area.py
from classDirector import Director

class Area(Director):
    def __init__(self):
        super().__init__()
        self._responsable = ""

    def set_responsable(self, responsable):
        self._responsable = responsable

    def get_responsable(self):
        return self._responsable