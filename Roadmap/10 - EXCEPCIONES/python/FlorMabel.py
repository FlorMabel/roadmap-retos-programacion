""" * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
"""
from python.Paprikaistkrieg import StringTypeError

#las excepciones se usan para evitar que el programa se detenga
#try: codigo que podria causar error ///  except: lo que hara el programa si ocurre error)
#ZeroDivisionError -  FileNotFoundError
try:
    print(10 /1)
    lista= [2,4,6,8]
    print(lista[5])
except Exception as error:
    print(f"Se produjo un error: {error}")

"""* DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
"""
print("*"* 20)
def parametros_varios(parametros: list):
    if len(parametros) < 6:
        raise IndexError
    elif parametros[4] == 0:
        raise ZeroDivisionError
    print(parametros[3])
    print(parametros[2]/parametros[5])
    print(parametros[4] + 3)

try:
    parametros_varios([2,0,6,8,'uno', 18])
except IndexError as error:
    print("El numero de la cantidad de la lista debe ser mayor")
except ZeroDivisionError as error:
    print("El numero no se puede dividir por cero")
except StringTypeError as error:
    print(f"{error}")
except Exception as error:
    print(f"Se ha producido un error {error}")
finally:
    print("El programa finalizo")
