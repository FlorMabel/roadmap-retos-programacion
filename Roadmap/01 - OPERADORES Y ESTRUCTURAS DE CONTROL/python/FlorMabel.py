#EJERCICIO:
# Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
# Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
# (Ten en cuenta que cada lenguaje puede poseer unos diferentes)

print("Operadores Aritméticos en Python")
print(f"Suma de 1 + 6 es: {1 + 6}")
print(f"Resta de 100 - 15.5 es : {100 - 15.5}")
print(f"Division de 6 / 4 es : {6/4}")
print(f"Division entera de 6 // 4 es: {6 //4}")
print(f"Modulo - residuo 6 % 4 es : {6%4}")
print(f"Multiplicacion 5 x 4 es: {5 * 4}")
print(f"Potenciacion de 2 sobre 3 es: {2 ** 3}")
print("\n")

print("Operadores Comparacion en Python")
print(f"5 sera igual '==' a 4: {5 == 4}")  # respuestas booleanas
print(f"3 desigualdad '!=' a 3: {3 != 3}")
print(f"2 sera mayor que 4: {2 > 4}")
print(f"2 sera menor que 4: {2 < 4}")
print(f"5 sera mayor o igual a 5: {5 >= 5}")
print(f"3 sera menor o igual a -3: {3 <= -3}")
print("\n")

print("Operadores Logicos en Python")
print(f"AND-&&: 8 + 2 == 10 and 3 - 7 == 4, esto es: {8 + 2 == 10 and 3 - 7 == 4}")
print(f"AND-&&: 8 + 2 == 10 and 17 - 7 == 10, esto es: {8 + 2 == 10 and 17 - 7 == 10}") # ambas deben ser True
print(f"OR-||: 3 + 2 == 5 or 2 - 6 == 4, esto es: {3 + 2 == 5 or 2 - 6 == 4}") # con un solo True es verdad
print(f"NOT-!: not 8 + 2 == 5, esto es: {not 8 + 2 == 5}")
print("\n")

print("Operadores Asignacion en Python")
numero = 3 # = asignacion
print(f"se inicia con el numero: {numero}")
numero += 2 # suma y asignacion
print(f"se le suma con += 2, el resultado es: {numero}")
numero -= 1 # resta y asignacion
print(f"se le resta con -= 1, el resultado es: {numero}")
numero *= 8 # multiplicacion y asignacion
print(f"se multiplica con *= 2, el resultado es: {numero}")
numero /= 2 # division y asignacion
print(f"Division entera con /= 4, el resultado es: {numero}")
numero //= 5 # division entera y asignacion
print(f"Division entera es con //= 2, el resultado es: {numero}")
numero %= 4 # modulo - residuo y asignacion
print(f"residuo o modulo %= 3, el resultado es: {numero}")
numero **= 4 # potenciacion y asignacion
print(f"potenciacion con **= 4, el resultado es: {numero}")
print("\n")

number=3
print("Operadores de Identidad IS - IS NOT en Python")
new_number = number # IS en este caso observa si ocupan la misma
print(f"number is new_number es: {number is new_number}") # RPT IS bool True
print(f"number is not new_number es: {number is not new_number}") #RPT IS NOT bool False

print("Operadores de Pertenencia IN -NOT IN en Python")
print(f"'f' in 'alforja': {'f' in 'alforja'}")
print(f"'j' not in 'alforja': {'J' not in 'alforja'}")

print("Operadores de Bit en Python")
#los bits lo convierten a binarios a 0 - 1
a = 10 # 1010
b = 3 #0011
print(f"AND: 10 & 3 = {10 & 3}")
print(f"OR: 10 | 3 = {10 | 3}")
print(f"XOR: 10 ^ 3 = {10 ^ 3}")
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")
# Utilizando las operaciones con operadores que tú quieras, crea ejemplos
# que representen todos los tipos de estructuras de control que existan
# en tu lenguaje:

print(f"Operadores de estructura de control condicional IF ELSE ELIF")
mi_nombre= "manrique"
if mi_nombre == "marique":
    print("mi_nombre es 'Manrique' ")
elif mi_nombre == "quispe":
    print("mi_nombre es Quispe")
else:
    print("No es manrique")

print(f"Operadores de estructuras Iterativas FOR - WHILE")

for i in range(11):   # tomara del 0 al 9 tendra los 10 numeros del rango
    print(i)

i = 0

while i <= 10:
  print(i)
  i += 1  # sin contador este bucle sera infinito
  
# Estructuras de control con excepciones
# basado en problemas que podria tener el codigo

try:
  print(10 / 0)
except:
  print("Se ha producido un error") # en caso de producir un error el mensaje
finally:
  print("Ha finalizado el recorrido") # si o si imprimira en caso de llegar al final
  
print('~' * 50)
# DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for i in range(10, 56):
  if i % 2 == 0 and i != 16 and i % 3 != 0:
    print(i)

# Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
