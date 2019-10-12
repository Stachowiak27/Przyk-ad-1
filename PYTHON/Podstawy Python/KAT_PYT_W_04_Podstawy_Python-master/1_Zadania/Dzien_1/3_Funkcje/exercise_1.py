# tutaj napisz funkcję z zadania 1

def square(num):
    return num*num

def square_print(num):
    print(num*num)

a = square(10)+10

b = square_print(10)+10

# Funkcja square zwraca wartość, dlatego wynik dodawania jest prawidłowy.
# Wynikiem funkcji square_print jest NONE, dlatego przy próbie dodawania wychodzi błąd.


print(a)
print(b)

# poniższe linijki przetestują Twoją funkcję:
print("2 podniesione do potęgi drugiej, to:", square(2))  # powinno być 4
print("16^2=", square(16))  # powinno być 256
print("256 do potęgi 2 =", square(256))  # powinno być 65536
 