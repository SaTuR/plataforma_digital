# ingrese un numero y diga si es par o impar
"""dotstring
1. pedir al usuario ingresar un numero
2. hcar el calculo para ver si es par o impar (variable % 2 == 0 es par  )
3. mostrar el mensaje
"""

numero = int(input("Ingrese un numero: "))

if (numero == 0):  # si el numero es igual a cero
    print("cero")
elif(numero % 2 == 0):  # caso contratio si el numero mod 2 es cero
    print("Es par")
else:  # caso contrario
    print("Es impar")
