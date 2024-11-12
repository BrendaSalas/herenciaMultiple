# director.py
class Director:
    def __init__(self):
        self._nombre = ""
        self._salario = 0.0

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_salario(self, salario):
        self._salario = salario

    def get_salario(self):
        return self._salario
