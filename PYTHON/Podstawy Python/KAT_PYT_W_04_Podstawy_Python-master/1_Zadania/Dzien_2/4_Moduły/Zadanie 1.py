
from random import randint

def d6(num):
    suma = 0
    for i in range(num):
        rzut = randint(1,6)
        print(rzut)
        suma = suma + rzut
    return suma

suma = d6(2)
print("===============")
print(suma)
