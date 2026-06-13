#estructuras por defecto
# EJERCICIO:
# Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# Utiliza operaciones de inserción, borrado, actualización y ordenación.

#LISTAS
lista =["emma", "loa", "merry"]
print(lista)

lista.append("timon")  # añadir al final insercion
print(lista)

lista.remove("emma") # remove/Elimina la cadena que se introduce
print(lista)

print(lista[0])  # indicamos que numero de indice imprimir

lista[1] = "canuto"# actualiza un dato que deseamos agregar y que cambie por el qu esta en ese indice
print(lista)

lista.sort() #ordena por alfabeto
print(lista)

#TUPLAS
tupla = ("core", "schnauzer", "toy", "sal pimienta", "17")
print(tupla[2]) # accedemos a lo que contiene en esa posicion
tupla = sorted(tupla) # el sorted cambia la tupla a lista pero su valores todas deben ser int o str, etc un solo tipo
print(type(tupla))
tupla = tuple(sorted(tupla)) # con esta accion ordena la tupla
print(tupla)

# SET ES UN TIPO DE ESTRUCTURA {}
# set se puede realizar varia acciones pero el set es estructura desordenada
mi_set={"Tomatillo", "Camotillo", "Pepinillo"}
mi_set.add("Arrocillo")# agrega
mi_set.add("Arrocillo")# por segunda vez pero set no permite duplicados y no volvera agregar
mi_set.remove("Pepinillo")
#Recordemos que set no se puede ordenar
print(mi_set)
print(type(mi_set))

#DICCIONARIO {}
mi_dic ={"nombre":"mary",
         "apellido":"pelinco",
         "edad":"10"}
#diccionario solo se puede acceder por clave
print(mi_dic["nombre"]) #para acceder
mi_dic["ciudad"]= "Huarmey" # para agregar o insertar
print(mi_dic)
mi_dic["edad"]= "11" # (actualizacion) seleccionando la edad se puede hacer los cambios
print(mi_dic)
del mi_dic["edad"]  # para eliminacion
print(mi_dic)
#para ordenar un diccionario antes no se debe perder el diccioanrio con sus valores
#primero continuamos con dict(sorted(----.items())) de esa manera se ordena y muestras tambien las claves
mi_dic = dict(sorted(mi_dic.items()))
print(mi_dic)

# DIFICULTAD EXTRA (opcional):
# Crea una agenda de contactos por terminal.
# Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
# Cada contacto debe tener un nombre y un número de teléfono.
# El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
# los datos necesarios para llevarla a cabo.
# El progr   ama no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
# (o el número de dígitos que quieras)
# También se debe proponer una operación de finalización del programa.

def agenda():
  mi_agenda = {"nombre": "tika", "apellido":"Orquidea","telefono":"990723861"}
  
  while True:
    print("1. Buscar Contacto")
    print("2. Insertar Contacto")
    print("3. Actualizar Contacto")
    print("4. Eliminar Contacto")
    print("5. Salir")
  
    opcion=input("\nSelecciona una Opcion: ")
  
    match opcion:
      case "1":
        nombre = input("Ingrese el nombre del contacto a buscar")
        if nombre in mi_agenda:
          print(f"el numero de telefono de {nombre} es {mi_agenda[nombre]}")
        else:
          print("El contacto que ingresaste no existe")
      case "2":
        nombre=input("\nIngrese el nombre del contacto: ")
        telefono=input("\nIngrese el Telefono del contacto: ")
        if telefono.isdigit() and len(telefono) > 0 and len(telefono) <=9:
          mi_agenda[nombre]=telefono
        else:
          print("Ingresaste datos errados, intenta otra vez")
      case "3":
        nombre = input("Ingresa el nombre del contacto a Actualizar")
        if nombre in mi_agenda:
          telefono = input("Ingresa el nuevo numero de telefono para actualizar")
          if telefono.isdigit() and len(telefono) > 0 and len(telefono) <=9:
            mi_agenda[nombre]=telefono
        else:
          ("Nombre de contacto no existe")
      case "4":
        nombre = input("Ingrese el nombre del contacto a eliminar")
        if nombre in mi_agenda:
          del mi_agenda[nombre]
          print(f"El contacto {nombre} a sido eliminado de {mi_agenda[nombre]}")
        else:
          print("El contacto que ingresaste no existe")
      case "5":
        print("Saliste de la agenda")
        break
      case _:
        print("Opcion Invalida, intente nuevamente")
    
  



agenda()