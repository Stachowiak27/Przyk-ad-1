

def cheesboard(n):
    for x in range(n):
        if x % 2 == 0:
            print (n*"# ")
        if x % 2 != 0:
            print (n*" #")

c = cheesboard(5)

print(c)