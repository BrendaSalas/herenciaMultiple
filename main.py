# main.py
from classDepartamento import Departamento
from classArea import Area
from classGerente import Gerente
from classJefeArea import JefeArea
from classEmpleado import Empleado
from classPersona import Persona
from classDirector import Director

def main():
    # Creación de objetos y asignación de valores
    director = Director()
    director.set_nombre("Juan Pérez")
    director.set_salario(5000)

    departamento = Departamento()
    departamento.set_nombre("Pedro López")
    departamento.set_salario(3000)
    departamento.set_area("Recursos Humanos")

    area = Area()
    area.set_nombre("Ana Gómez")
    area.set_salario(2500)
    area.set_responsable("Juan Pérez")

    gerente = Gerente()
    gerente.set_nombre("Carlos Fernández")
    gerente.set_salario(4000)
    gerente.set_departamento("IT")

    jefe_area = JefeArea()
    jefe_area.set_nombre("Luis Martínez")
    jefe_area.set_salario(3500)
    jefe_area.set_equipo("Equipo de Soporte")

    empleado = Empleado()
    empleado.set_nombre("Marta Díaz")
    empleado.set_salario(2000)
    empleado.set_puesto("Analista")
    empleado.set_antiguedad(5)

    persona = Persona()
    persona.set_nombre("José López")
    persona.set_edad(30)

    # Imprimir información
    print(f"Director: {director.get_nombre()} con salario de {director.get_salario()}")
    print(f"Departamento: {departamento.get_area()} dirigido por {departamento.get_nombre()}")
    print(f"Área: {area.get_responsable()} tiene como responsable a {area.get_nombre()}")
    print(f"Gerente: {gerente.get_nombre()} del departamento {gerente.get_departamento()}")
    print(f"Jefe de Área: {jefe_area.get_nombre()} dirige el equipo {jefe_area.get_equipo()}")
    print(f"Empleado: {empleado.get_nombre()} trabaja como {empleado.get_puesto()} con {empleado.get_antiguedad()} años de antigüedad")
    print(f"Persona: {persona.get_nombre()} tiene {persona.get_edad()} años")

if __name__ == "__main__":
    main()
