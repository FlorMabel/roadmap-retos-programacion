""" * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal."""
#Herencia: permite a una clase (hija o subclase) heredar atributos y metodos - facilita la reutilizacion
#Polimorfismo: varios metodos con el  mismo nombre pero con distintos parametros
#dar una misma orden a diferentes objetos y cada uno lo cumple o responde a su manera

class Animal:
    def __init__(self, name: str ):
        self.name = name
    def sonido(self):
        #print("El sonido que emite aun no se puede determinar")
        pass
#sub clase
class Gallo(Animal):
    def sonido(self):
        print("kokoroco")

class Pollo(Animal):
    def sonido(self):
        print("Pio Pio")

def print_sonido(animal: Animal):
    animal.sonido()
"""
mi_animal = Animal("Animal")
mi_animal.sonido()
mi_animal = Gallo("Gallo")
mi_animal.sonido()
mi_animal = Pollo("Pollo")
mi_animal.sonido()
"""
mi_animal = Animal("Animal")
print_sonido(mi_animal)
mi_Gallo = Gallo("Gallo")
print_sonido(mi_Gallo)
mi_pollo = Pollo("Pollo")
print_sonido(mi_pollo)

"""
class Gallo:
    def __init__(self, name: str ):
        self.name = name
    def sonido():
        print("kokoroco")

class Pollo:
    def __init__(self, name: str ):
        self.name = name
    def sonido():
        print("Pio Pio")
"""
""" DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo."""

class Empleado:
    def __init__(self, id: int, name:str):
        self.id = id
        self.name = name
        self.empleados = []

    def add(self, empleado):
        self.empleados.append(empleado)

    def print_empleados(self):
        for empleado in self.empleados:
            print(empleado.name)
class Gerente(Empleado):
    def coordinacion_proyectos(self):
        print(f"{self.name}, Coordina todos los proyectos de la Empresa")


class Gerente_proyec(Empleado):
    def __init__(self, id: int, name: str, proyecto: str):
        super().__init__(id, name)
        self.proyecto = proyecto

    def coordina_proyecto(self):
        print(f"{self.name}, Coordina solo su propio proyecto")


class Programador(Empleado):
    def __init__(self, id: int, name: str, lenguaje: str):
        super().__init__(id, name)  #llamamos los parametros del padre
        self.lenguaje = lenguaje

    def programa(self):
        print(f"{self.name}, Programa un proyecto asignado en {self.lenguaje} ")

    def add(self, empleado: Empleado):
        print(f"El programador no tiene empleados a su cargo: {empleado.name}")

    def code(self):
        print(f"{self.name}, esta programando en {self.lenguaje}")



mi_gerente = Gerente(1, "Teodoro")
mi_gerente_proyec = Gerente_proyec(2, "Manrique", "Proyecto: WEB")
mi_gerente_proyec2 = Gerente_proyec(3, "Garcia", "Proyecto: SISTEMA VENTA")
mi_programador = Programador (4, "Robles", "Python")
mi_programador2 = Programador (5, "Mendoza", "JavaScrip")
mi_programador3 = Programador (6, "Enriquez", "C++")
mi_programador4 = Programador (7, "Gutierrez", "Java")

mi_gerente.add(mi_programador)
mi_gerente.add(mi_programador2)

mi_gerente_proyec.add(mi_programador)
mi_gerente_proyec.add(mi_programador2)
mi_gerente_proyec.add(mi_programador3)
mi_gerente_proyec.add(mi_programador4)

mi_programador.add(mi_programador2)

mi_programador.code()
mi_gerente_proyec.coordina_proyecto()
mi_gerente.coordinacion_proyectos()
mi_gerente.print_empleados()