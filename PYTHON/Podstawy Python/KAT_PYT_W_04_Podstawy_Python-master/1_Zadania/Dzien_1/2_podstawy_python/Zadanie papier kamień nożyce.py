
import random

a = int(input("Podaj 1-kamień, 2- nożyce lub 3- papier  "))

number_computer = random.randint(1,3)
print("Komputer podał:",number_computer)

if a == number_computer:
    print("Remis")
elif a == 1 and number_computer == 2:
    print("Wygrałeś")
elif a == 2 and number_computer == 3:
    print("Wygrałeś")
elif a == 3 and number_computer == 1:
    print("Wygrałeś")
elif a > 3:
    a = int(input("Wprowadziłeś błędną liczbę, podaj 1-kamień, 2- nożyce lub 3- papier  "))
else:
    print("Wygrywa komputer")