

def mean(numbers):
    suma = 0
    for item in numbers:
        suma = item + suma
        average = suma/len(numbers)
    return average

numbers = [2,4,5,7,8]

new = mean(numbers)

print(new)

def mean(numbers):
    for item in numbers:
        return sum(numbers)/len(numbers)

print("średnia wynosi =",new)