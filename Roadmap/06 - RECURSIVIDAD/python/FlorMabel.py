"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
"""
#recursividad: cuando la funcion se llama asi misma para resolver el problema

def descontar(num):
    if num == 0:   #100
        print("0 - Llegaste a la Meta")
        return
    print(num)
    descontar(num - 1)
    #contar(num + 1)

#contar(0)
descontar(100)

"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
"""
#factorial: multiplica un numero por todos sus numeros menores
#ejemplo 4 x 3 x 2 x 1 = 24  // n! = n * (n - 1)!
print("\n***** Factorial *****")

def factorial(num: int):
    acumulador = 1

    for i in range(1, num +1):
        acumulador *= i

    return acumulador
print(f"El resultado es: {factorial(4)}")

print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
#validando que no sea menor a cero
def facto(numero: int) -> int:
    if numero < 0:
        print(f"{numero} es negativo")
    elif numero == 0:
        return 1
    else: return numero * facto(numero - 1)

print(f"El resultado es: {facto(6)}")

#Sucesion de Fibonacci
#la suma de numeros, cada numero se obtiene de la suma de los anteriores
#eje: 0,1,1,2,3,5,8,13.......
#en este modelo desglozamos los numeros
print("*** Fibonacci con For v1 ***")
def fibo(n):
    x = 0
    y = 1
    for i in range(n):
        print(x)
        temp = x
        x = y
        y = temp + y
    return
fibo(6)

# en este modelo se tendra el valor final
print("\n*** Fibonacci con For v2 ***")
def fibon(n):
    x = 0
    y = 1
    for i in range(n):
        temp = x
        x = y
        y = temp + y
    return x
print(f"El valor final de 8: {fibon(8)}")

#
print("\n*** Fibonacci v3 ***")

def fibonacci(num:int)->int:
    if num <= 0:
        print(f"El Numero debe ser mayor a:{num} ")
        return 0
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num -1) + fibonacci(num - 2)

print(f"El resultado es: {fibonacci(8)}")