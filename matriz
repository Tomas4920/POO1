def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()

filas = int(input(" Filas de la matriz: "))
columnas = int(input(" Columnas de la matriz: "))

matriz = [[0] * columnas for _ in range(filas)]
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = i * columnas + j + 1

print(" Matriz: ")
imprimir_matriz(matriz)
