""" * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 """
"""OPERACIONES"""
#CONCATENACION
uno= "Hola"
dos = "Core"
print(uno + " " + dos+"!")

# repeticion de cadenas de txt
print(f"~~ {uno * 4} ~~" )

#indexacion de caracteres
print(uno[0]  + uno[3])
print(dos[-2]) # busca desde el lado derecho e inicia en -1

#longitud de una cadena
print(len(dos))

#Slacing (opcion)
print(dos[2:5])
print(dos[1:2])

#busqueda
print("r" in dos)
print("a" in dos)
print("la" in uno)

#Reemplazar - quitar espacios
print(uno.replace("H","C"))
print(dos.strip()) #quita espacios del inicio y del final

#Division (corta donde se le indique )
print(uno.split("l"))

#mayúsculas - minúsculas - primera letra mayúscula
print(uno.upper())
print(uno.lower())
print("carrera de caracoles".title())  # primera cada letras mayusculas
print("carrera de caracoles".capitalize())  # solo la primera letra mayuscula

#elimacion de espacios al final e inicio
print("  Camino al Dorado   ")
print("  Camino al Dorado   ".strip())
print("  Camino al Dorado   ".strip() + "**" )

#busqueda de el principio y el final
print(dos.startswith("co"))
print(uno.startswith("Ho"))
print(uno.endswith("a"))
print(dos.endswith("re"))

#encontrar la posición (indice)
print("Camino al Dorado".find("no"))
print("Camino al Dorado".find("ca"))
print("Camino al Dorado".lower().find("ca"))

tres = "CORE corre corre y ladra"
#busqueda de ocurrencias
print(tres.lower().count("ladra"))
print(tres.upper().count("CORE"))
print(tres.count("r"))

#formateo
print("Hermoso:{} , Dia:{}".format(uno, dos))

#interpolación
print(f"Hermoso:{uno} , Dia:{dos}")

#transformación en lista de caracteres
print(list(tres))

#transformacion de lista en cadena
todo = (uno, " ,", dos, " ,", tres, "***")
print("~".join(uno))
print("~".join(todo))

#transformaciones numericas
st_num = "1234567890"
nu_num = int(st_num)
print(st_num)

st_num = "1234.567890"
#nu_num = float(st_num)
print(st_num)

#comprobaciones validas
print(uno.isalnum())
print(uno.isalpha())
print(st_num.isalpha())

#verificacion de contenido
texto = "camino @l dorado"
print("@" in texto)  #buscara si existe dentro del texto
print(texto.startswith("m"))
print("890".isdigit()) # para preguntar si es numerico

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos = se lee igual de derecha a izquierda
 * - Anagramas = palabras o frases que reorganizando nueva palabra o frase
 * - Isogramas = palabra que ninguna letra se repite
"""
def check(escrito1: str, escrito2: str):

    #palindromo
    print(f"{escrito1} es un palindromo?: {escrito1 == escrito1[::-1]}")
    print(f"{escrito2} es un palindromo?: {escrito2 == escrito2[::-1]}")



    #anagrama
    print(f"{escrito1} es un anagrama de {escrito2}?: {sorted(escrito1) == sorted(escrito2)}")

    #isograma
    print(f"{escrito1} es un isograma?: {len(escrito1) == len(set(escrito1))}")
    print(f"{escrito2} es un isograma?: {len(escrito2) == len(set(escrito2))}")

    escrito_dict = dict()
    for escrito in escrito2:
        escrito_dict[escrito] = escrito_dict.get(escrito, 0) + 1
        #print(escrito)
    print(escrito_dict)

    isograma = True
    #print(escrito_dict.items())
    #print(escrito_dict.keys())
    #print(escrito_dict.values())

    values = list(escrito_dict.values())
    isograma_len = values[2]
    for escrito_count in escrito_dict:
        if len(escrito_count) != isograma_len:
            isograma = False
            break
    print(isograma)

    print(escrito_dict)

#check("reconocer", "reconocer")
check("reno", "apellido")
#check("oido", "odio")
