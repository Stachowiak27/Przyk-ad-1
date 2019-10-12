import random

rows = random.randint(5,15)
columns = random.randint(5,15)

print("Wartość zmiennej rows:",rows)
print("Wartość zmiennej columns:",columns)



for item in range(rows):
    for item in range(columns):
        print("*",end="")
    print("\n",end="")