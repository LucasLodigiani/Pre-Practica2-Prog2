#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

print("Ingrese 4 pares o impares")
lista = []
listaImpar = []
for i in range(10):
    lista.append(int(input()))

    if (lista[i] % 2 != 0):
        listaImpar.append(lista[i])


print("Lista par original: " + str(lista))
print("Lista impar copia: " + str(listaImpar))
#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO

#FIN