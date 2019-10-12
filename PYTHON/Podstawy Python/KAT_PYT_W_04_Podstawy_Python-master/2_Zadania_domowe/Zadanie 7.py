
lista=[2,4,3]

def histogram(lista):
    temp = []
    for item in lista:
        temp.append("#" * item)
    return "\n".join(temp)


print(histogram(lista))