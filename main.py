#Programa para saber si un numero es par o impar
print("----------*Enoc Carrera ©2021*----------")
print("Este programa le ayudaraa saber si un numero es par o impar \n")
numero = int(input("Ingrese un numero: \n"))
#Operacion: si la division no tiene residuo el numero es par , si la division tiene residuo el numero es impar
resultado = numero % 2
if resultado == 0:
    print(f"El numero: {numero} es par \n")
    print("Gracias por utilizar nuestro software :)")
else:
    print(f"El numero: {numero} es impar \n")
    print("Gracias por utilizar nuestro software :)")