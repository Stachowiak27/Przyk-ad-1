
def findboundaries(lista):

    lista = [item for item in lista if type(item)==int]
    new_list = (max(lista),min(lista))
    return new_list

c = findboundaries([3,6,8,9,-1])

print(c)

c = findboundaries([0,2,"a kuku", 10])

print(c)