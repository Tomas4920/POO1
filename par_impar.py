def par(num):
    if num % 2 == 0:
        return True
    else:
        return False

num_dig= int(input(" Digite un número: "))

if par(num_dig):
    print(f" {num_dig} es par.")
else:
    print(f" {num_dig} es impar.")
