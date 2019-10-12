
def circle_circuit(kaliber):
    r = kaliber/2
    # o = obwód
    pi = 3.14
    o = 2 * pi * r
    return o

kaliber = 12

print("Obwód koła o średnicy:",kaliber,"wynosi:",(circle_circuit(kaliber)))
