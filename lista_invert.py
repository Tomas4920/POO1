def invert_lista(lista):
    lista_invert = lista[::-1]
    return lista_invert

entrada = input(" Ponga los elementos: ")
elementos = entrada.split()

# Invertir el orden de los elementos en la lista
lista_invert = invert_lista(elementos)

# Mostrar la lista invertida
print("Lista invertida:", lista_invert)

