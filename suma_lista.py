def calcular_suma(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

entrada = input(" Digite los números que desea sumar: ")
num = [int(num) for num in entrada.split()]

suma_total = calcular_suma(num)

print(" Resultado de la suma: ", suma_total)
