
def is_even(number):
    return number % 2 == 0


print(is_even(21))

def iterate_true(number):
    for i in range(1,number):
        print(is_even(i))

iterate_true(20)



