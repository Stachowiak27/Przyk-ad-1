
numbers = [2,4,6,3,45,65]

def suma(numbers):
    for item in numbers:
        return sum(numbers)

print(suma(numbers))



def suma(numbers):
    suma = 0
    for item in numbers:
        suma = suma + item
    return suma

print("Suma = ",suma(numbers))