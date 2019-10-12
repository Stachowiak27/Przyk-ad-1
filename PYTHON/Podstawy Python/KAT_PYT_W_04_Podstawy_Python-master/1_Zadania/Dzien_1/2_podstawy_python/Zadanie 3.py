import random

no_of_stars = random.randint(0,20)

print("Wylosowana liczba:",no_of_stars)


for x in range(no_of_stars):
    print("*",end="")

