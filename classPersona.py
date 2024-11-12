# persona.py
class Persona:
    def __init__(self):
        self._nombre = ""
        self._edad = 0

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_edad(self, edad):
        self._edad = edad

    def get_edad(self):
        return self._edad
