
lista = ['Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie']


def find_short_words(lista):
        l = []
        for words in lista:
            if len(words) < 5:
                l.append(words)
        return l

print(find_short_words(lista))



def find_short_words(my_list):
    new_list = []
    for words in my_list:
        if len(words) < 5:
            new_list.append(words)
    return new_list

a = find_short_words(lista)
print(a)