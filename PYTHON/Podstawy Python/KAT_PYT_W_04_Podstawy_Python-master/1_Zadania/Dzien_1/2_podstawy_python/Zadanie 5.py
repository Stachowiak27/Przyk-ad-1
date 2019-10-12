import random

size = random.randint(3,9)

print(size)

for x in range(size):
    for x in range(x+1):
        print("*",end="")
    print("\n",end="")

print("--------------------------")

for x in range(size):
    for x in range(size-x):
        print("*", end="")
    print("\n", end="")



