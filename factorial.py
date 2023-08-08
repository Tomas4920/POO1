def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, num + 1):
            factorial *= i
        return factorial

num_dado = int(input(" Numero para calcular su factorial: "))

factorial_calc = factorial(num_dado)

print(f"El factorial de {num_dado} es {factorial_calc} ")
