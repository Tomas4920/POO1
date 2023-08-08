def maximo_minimo(lista):
    max = float('-inf')
    min = float('inf')

    for num in lista:
        if num > max:
            max = num
        if num < min:
            min = num

    return max, min

entrada = input("Digite los números: ")
num = [int(num) for num in entrada.split()]

max, min = maximo_minimo(num)

print("El número más grande es:", max)
print("El número más pequeño es:", min)

