""" * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.  """
#clase: es una plantilla o molde para crear objetos
#objeto: una instancia 'especifica' creada a partir de la clase
#atributos: las variables que almacenan las caracteristicas del objeto
#métodos: la funcion dentro de la clase que define lo que pede hacer
#permite organizar al agrupar datos y funciones // reutilizar codigo // mantener los datos de forma independiente
#NOTA: por convencion la primera letra de la clase se escribe en MAYÚSCULA

#defincion de la clase o inicializador
class Maestro:
#Atributo fuera del constructor se puede agregar y darle valor NONE, "" ,etc.
    apellido:str = ""

# metodo constructor
    def __init__(self, nombre:str, edad:int, idioma:list):
        self.nombre = nombre  #atributo
        self.edad = edad
        self.idioma = idioma

#metodo (comportamaniento)
    def print(self):
        print(f"Nombre: {self.nombre} | Apellido: {self.apellido} | Edad: {self.edad} | Idioma: {self.idioma}")

#creacion del objeto (instancia) se puede agregar el atributo que se creo fuera
mi_maestro = Maestro("Scott", 70, ["Python", "JavaScript", "C++"])

#accediendo a los atributos y metodos
mi_maestro.print()
mi_maestro.apellido = "Alpino"
mi_maestro.print()
mi_maestro.edad = 67  # modificacion
mi_maestro.print()

""" DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 * retornar el número de elementos e imprimir todo su contenido. """
#pila -LIFO
print("\n¨¨¨¨¨¨¨ PILA - LIFO ¨¨¨¨¨¨¨¨¨")
class Stack:
    def __init__(self):
        self.stack = []  #pila vacia
#agregar
    def push(self, item):
        self.stack.append(item)

#eliminar
    def pop(self):
        if self.retorno() == 0:
            return None
        return self.stack.pop()

#retornar
    def retorno(self):
        return len(self.stack)

#impresion // se coloca en reversa por ser una pila
    def imprimir(self):
        for item in reversed (self.stack):
            print(item)

mi_stack = Stack()
mi_stack.push(11)
mi_stack.push(21)
mi_stack.push("33")
print(mi_stack.retorno())
mi_stack.imprimir()
print("\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
mi_stack.pop()
print(mi_stack.retorno())
mi_stack.imprimir()
print("\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
mi_stack.pop()
mi_stack.pop()
print(mi_stack.retorno())
mi_stack.imprimir()

#cola FIFO
print("\n¨¨¨¨¨¨¨ COLA - FIFO ¨¨¨¨¨¨¨¨¨")
class Queue:
    def __init__(self):
        self.queue = []

#agregar
    def equeue(self, item):
        self.queue.append(item)

#quitar
    def deequeue(self):
        if self.mostrar() == 0:
            return None
        return self.queue.pop(0)

#mostrar
    def mostrar(self):
        return len(self.queue)

# impresion //
    def imprime(self):
        for item in (self.queue):
            print(item)

mi_queue = Queue()
mi_queue.equeue(1)
mi_queue.equeue(2)
mi_queue.equeue("3")
print(mi_queue.mostrar())
mi_queue.imprime()
print("\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
mi_queue.deequeue()
print(mi_queue.mostrar())
mi_queue.imprime()
print("\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
mi_queue.deequeue()
mi_queue.deequeue()
print(mi_queue.mostrar())
mi_queue.imprime()
