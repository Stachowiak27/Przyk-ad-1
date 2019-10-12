
number = int(input("Podaj liczbę:"))

def is_divided_by_4(number):
    if number % 4 == 0:
        return True
    else:
        return False

print(is_divided_by_4(number))
