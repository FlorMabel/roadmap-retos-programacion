""" VALOR Y REFERENCIA
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 Por referencia: se pasa la direccion de memoria y esta SI afecta al original
  """
# Por valor: copia el valor - las modificaciones no afectan al original
val_int_a = 5
val_int_b = val_int_a
val_int_b = 25
val_int_a = 15
print(val_int_a)
print(val_int_b)

#Por referencia: se pasa la direccion de memoria y esta SI afecta al original
list_a = [10,30]
list_b = [20,40,100]
list_a = list_b
list_a.append(60)
list_c = [1,1,1,1]
list_b = list_c
print(list_a)
print(list_b)
print(list_c)
"""
* - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
"""
#funcion con datos de valor
print("\n***************************\n")
lisA=15

def lis_fun(lis: int):
    lis = 30
    print(lis)

lis_fun(lisA)
print(lisA)

#funcion con datos de referencia
print("\n***************************\n")

referen = [3,5]

def referen_fun(list_refe: int):
    list_refe.append(2)
    list_refe.insert(0,9)
    print(list_refe)

referen_fun(referen)
print(referen)

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 """
#Valor
v_uno = 15
v_dos = 10

def valor(valor1: int, valor2: int):
    temp = v_uno
    valor1 = v_dos
    valor2 = temp
    return valor1 , valor2

valor1, valor2 = valor(v_uno, v_dos)
print(f"original valor uno: {v_uno} y valor dos: {v_dos} ")
print(f"cambio valor uno: {valor1} y valor dos: {valor2} ")

#referencia

uno = [2,4]
dos = [1,0]


def referencia(val1: int, val2: int):
    tempo = uno
    val1 = dos
    val2 = tempo
    val1.append(8)
    val2.insert(0, 10)
    return val1 , val2

val1, val2 = referencia(uno, dos)
print(f"original valor uno: {uno} y valor dos: {dos} ")
print(f"cambio valor uno: {val1} y valor dos: {val2} ")





