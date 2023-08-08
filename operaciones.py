num1 = float(input(" Primer número: "))
num2 = float(input(" Segundo número: "))

suma = num1 + num2
resta = num1 - num2
mult = num1 * num2

if num2 != 0:
    div = num1 / num2
else:
    div = "No se puede dividir con el cero"

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {mult}")
print(f"División: {div}")
