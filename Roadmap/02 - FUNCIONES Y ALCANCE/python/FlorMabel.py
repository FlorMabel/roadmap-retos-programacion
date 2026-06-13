#EJERCICIO:
# Crea ejemplos de funciones básicas que representen las diferentes
#posibilidades del lenguaje:
#   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
# - Comprueba si puedes crear funciones dentro de funciones.
# - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
# - Pon a prueba el concepto de variable LOCAL y GLOBAL.
# - Debes hacer print por consola del resultado de todos los ejemplos.
#   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
#FUNCIONES DEFINIDAS POR EL USUARIO
#SIMPLE
def saludo():
    print("Hola Python")
saludo()

# CON RETORNO
def return_saludo():
    return "Hola my Python"
#saludo = return_saludo() # un forma de imprimir es esta guardando en una variable
#print(saludo)
print(return_saludo()) # segunda forma de imprimir dentro de print

#FUNCION CON ARGUMENTO
def arg_saludo(nombre):
    print(f"hola {nombre}")
arg_saludo("Caracol")

#FUNCION CON MAS DE UN ARGUMENTO
def arg_saludo(saludo, nombre):
    print(f"primero {saludo}, {nombre}")
arg_saludo("Hello", "estimado")

#FUNCION CON ARGUMENTO PREDETERMINADO o por defecto
def prede_arg_saludo(apellido = "Manrique"):
    print(f"Hola, {apellido}")

prede_arg_saludo("Core") # se coloca su valor
prede_arg_saludo() # en la funcion se coloca por defecto y solo se imprime por defecto

#FUNCION CON MULTIPLES VALORES
def multiple_return_saludo():
    return "VAMOS", "BIEN"
#print(multiple_return_saludo())# el return saldra dentro de parentesis
saludo, nombre = multiple_return_saludo()
print(saludo) #immprime primero vamos
print(nombre) #segunda impresion bien

#FUNCIONES BASICA CON UN NUMERO VARIABLE DE ARGUMENTOS
def var_argumento_saludo(*nombres):   #*indica que podemos darle mas de un nombre o argumento
    for nombre in nombres:
        print(f"Hola, {nombre}")
var_argumento_saludo("Codigo", "Python", "Flor", "Stich")

#FUNCIONES CON UN NUMERO DE VARIABLE DE ARGUMENTO CON PALABRA CLAVE
def var_key_argumento_saludo(**nombres): #**indica clave a cada argumento tendra un valor
    for key, value in nombres.items():
        print(f"Hola, {value} ({key})")
      
var_key_argumento_saludo(
    Escritura="Codigo",
    Lenguaje="Python",
    Nombre="Flor",
    Peluche="Stich" )

#FUNCIONES DENTRO DE FUNCIONES
def principal_funcion():
    def interior_funcion():
        print("funcion interna: Codigo Python")
    interior_funcion()
      
principal_funcion()

#FUNCIONES DEL LENGUAJE (ESTAN CONSTRUIDAS DENTRO DEL LENGUAJE)
#matematicas
print("\n FUNCIONES MATEMATICAS")
print("valor absoluto de 156353",abs(156353))
print("potencia (2,3)",pow(2,3))
print("redondeo de 5.7",round(5.7))
print("el minimo de 2,5,-1 es: ",min(2,5,-1))
print("el  maximo de -2,5,9 es: ",max(-2, 5,9))
print("La suma de  ([2,7]) es: ",sum([2,7]))

#conversion de tipos
print("\nCONVERSION DE TIPO DE DATOS")
print("string '3' se convertira a int: ",int("3"))
print("string float '2.6' a deciomal: ", float("2.6"))
print("Una cadena: ", str("jueves"))
print("sera verdad '0': ",bool(0))
print("Lista: ",list("ayz"))
print("tupla ([2,4,6]): ",tuple([2,4,6]))

#estructura de datos
print("\nESTRUCTURA DE DATOS")
print("longitud de numeros ([2,3,4,5]): ",len([2,3,4,5]))
print("longitud de texto 'codificacion: '",len("Codificacion"))
print("sorted ordena numero([4,7,1,3])",sorted([4,7,1,3]))
letras=['w','a','g','e']
peso =[119, 97,103, ]
print("sorted ordena caracteres ['w','a','g','e])",sorted(letras))
print("list(enumerate(letras)) hara que se enumere cada letra: ",list(enumerate(letras)))
print("list(zip(letras,peso)) empareja entre las dos listas y termina con la mas corta: ",list(zip(letras,peso)))

#logica y validacion
print("\nFUNCION DE LOGICA Y VALIDACION")
print("muestra el tipo de dato type(): ",type("jojojo"))
print("isinstance(10, int) - para comprobar el tipo de dato si en T o F: ",isinstance(10, int))
print("all 'TRUE'si todos son T (t,f,f): ",all([True, False, False]))
print("any 'TRUE' su al menos hay un T (f,t,t): ",any([False, True, True]))

#iteracion
print("\nFUNCION RELACIONADAS CON ITERACION")
print("Imprimi una lista con el rango que determinamos list(range(1,5): ",list(range(2,5)))
print("accede al primer numero de la lista generada next(iter([10, 20, 30])): ",next(iter([10, 20, 30])))

#avanzadas
print("\nFUNCION AVANZADAS")
print("map tomara cada uno de la lista y le dara 'x' para que se multiplique * 2")
print("list(map(lambda x: x * 2, [1, 2, 3]))")
print(list(map(lambda x: x * 2, [1, 2, 3])))
print("filter tomara cada dato de la lista para 'x'y lo compara con >2 para T o F")
print("list(filter(lambda x: x > 2, [1, 2, 3, 4])) imprimira solo los mayores a 2")
print(list(filter(lambda x: x > 2, [1, 2, 3, 4])))
print("en este caso 'x' tomara el valos de 5 y lo sumara con lo indicado")
print("(lambda x: x + 1)(5)")
print((lambda x: x + 1)(5))
print("eval abre las comillas y entiende que es un suma eval('2' +'3'): ",eval("2 + 3"))

#funciones del sistema y ayuda
print("\n (dir()) devuelve una lista con todos los nombres de los metodos y atributos\n"
     "si lo usas en una lista vacia[], te muestra todo lo que puedes hacer ")
ciudad = ["Arequipa", "Tumbes", "Tacna"]
print(dir(ciudad))

print("\n .__doc__ Explica la documentacion interna de la funcion de lo que hace \n"
      " puede ser len, map, etc. explicacion de lo que hara la funcion ")
print(map.__doc__)

print("\n id() devuelve el  identificador unico de un objeto en memoria  \n"
      " id(5) el numero representa la ubicacio del objeto dn memoria ")
print(id(3))  #140715183522792 identicador de memoria
print(id(15)) #140715183523176
print(id("z")) #140715183588496

#FUNCIONES QUE MODIFICAN
print("\n APPEND() agrega a la derecha lista.append(9)")
lista = [1,3,0,4,11,5,2,6,8]
lista.append(9)
print(lista)

print("\n INSERT() inserta en la posicion que desees lista.insert(a,b)")
lista.insert(4,29)
print(lista)

print("\n REMOVE() elimina el caracter o dato indicado que deseas lista.remove(4)")
lista.remove(4)
print(lista)

print("\n POP() elimina por indice lista.pop(6)")
lista.pop(6)
print(lista)

print("\n SORT() ordena la lista.sort()")
lista.sort()
print(lista)

print("\n REVERSE() revierte el orden lista.reverse(4)")
lista.reverse()
print(lista)

print("\n CLEAR() vacia toda la lista lista.clear()")
lista.clear()
print(lista)

#MODIFICACION DE DICCIONARIOS
print("\n UPDATE() - diccionario agrega o actualiza update({})")
dic = {"a": 1}
dic.update({"b": 2})
print(dic)

print("\n pop() - diccionario elimina una clave dicc.pop('a')")
dicc = {"a": 1, "b":2}
dicc.pop("a")
print(dicc)

print("\n CLEAR() - vacia el diccionario dicc.clear('a')")
dicc = {"a": 1, "b":2}
dicc.clear()
print(dicc)
#METODOS QUE MODIFICAN CONJUNTOS
print("\n ADD() - agrega elemento conjunto.add(5)")
conjunto = {1,2,3}
conjunto.add(5)
print(conjunto)

print("\nREMOVE - Elimina elemento conjunto.remove(2)")
conjunto.remove(2)
print(conjunto)

print("\n UPPER() - cambia todo a mayuscula 'camilo cesto'.upper()")
print("camilo cesto".upper())
print("\n LOWER() - cambia todo a minuscula 'CAMILO CESTO'.upper()")
print("CAMILO CESTO".lower())
print("\n CAPITALIZE() - cambia la primera letra a mayuscula 'camilo cesto'.upper()")
print("camilo cesto".capitalize())
print("\n TITLE() - cada palabra la inicial a mayuscula 'camilo cesto'.upper()")
print("camilo cesto".title())

#VARIABLES LOCALES Y GLOBALES
global_var = "global"

print(global_var)

def python():
    local_var = "local"
    print(f"{local_var}, {global_var}") # esta variable esta fuera de la funcion
print(global_var)
#print(local_var)# no funcionara por sole funciona dentro del ambito local
python()


# DIFICULTAD EXTRA (opcional):
# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
#
# Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
# Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
def extra(text1,text2)-> int:
    contador = 0
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print(text1 + text2)
        elif num % 5 ==0:
            print(text2)
        elif num % 3 == 0:
            print(text1)
        else :
            print(num)
            contador += 1
    return contador
print(extra("fizz ", "buzz"))
