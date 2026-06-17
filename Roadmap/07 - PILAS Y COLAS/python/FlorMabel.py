""" * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 """
#Pila: el ultimo en ingresar es el primero en salir
# push: agregar // pop: eliminar el ultimo que ingreso
print("\n ******* PILAS - STACKS - LIFO *******")
#push
pila = []
pila.append("dos")
pila.append(2)
pila.insert(0 ,6)
print(pila)

#pop
pila_item = pila[len(pila)-1]
del pila[len(pila)-1]
print(pila_item)

print(pila.pop())
print(pila)

print("\n ******* COLAS - QUEUE - FIFO *******")
#cola: el primero en entrar es el primero en salir
# enqueue: agregar al final // dequeue: eliminar al primero-
#recomendable usar collections.deque (agregar o eliminar de ambos extremos)
cola = []
#push
cola.append("tres")
cola.append(3)
cola.append(4)
cola.insert(2 ,8)

#dequeue
print(cola)
print(cola.pop(0))
cola_item = cola[0]
del cola[0]
print(cola_item)
print(cola)


"""
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web. """
print("\n************** PRIMER RETO - PILA *******************\n")
 # web de navegacion

def web_navegador():
    pila = []

    while True:
        direccion = input("Ingresa la url o interactúa palabra atras / adelante / salir para continuar:")
        if direccion == "salir":
            print("Gracias por la visita esta saliendo de la sesión")
            break
        elif direccion == "adelante":
            pass#Una vez que se retrocede con 'pop' se elimina por lo que adelante
            # No se podria usar la pila en adelante si se retrocedio
        elif direccion == "atras":
            if len(pila) > 0:
                pila.pop()
        else:
            pila.append(direccion)

        if len(pila)>0:
            print(f"Estas en la siguiente url: {pila[len(pila)-1]}")
        else:
            print("Estas en la sección de Inicio")



web_navegador()

"""
 # Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 # impresora compartida que recibe documentos y los imprime cuando así se le indica.
 # La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 # interpretan como nombres de documentos. """

print("\n************** SEGUNDO RETO - COLA *******************\n")
def web_impreso():
    cola = []

    while True:
        ingresa = input("Agrega un documento o selecciona imprimir/salir: ")
        if ingresa == "salir":
            print("Saliste del sistema, hasta pronto")
            break
        elif ingresa == "imprimir":
            if len(cola)>0:
                print(f"Se imprime este documento {cola.pop(0)}")
        else:
            cola.append(ingresa)
        print(f"Este la cola de impresion: {cola}")

web_impreso()