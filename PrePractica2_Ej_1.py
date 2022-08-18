#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO
print("Ingrese el primer numero")
n1 = int(input())
print("Ingrese el segundo numero")
n2 = int(input())


maximo = max(n1, n2)
print("El maximo es: " + str(maximo))

#FIN