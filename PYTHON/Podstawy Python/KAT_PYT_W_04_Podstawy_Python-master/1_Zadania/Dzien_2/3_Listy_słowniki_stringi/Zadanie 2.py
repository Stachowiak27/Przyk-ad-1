
def list_keys(d):
    a = []
    for key in d:
        a.append(key)
    return a

d = {"KIA": "Sportage","VW":"Golf", "Alfa Romeo":"156 GTA"}


print(list_keys(d))
print(list(d.keys()))
print(list(d.values()))
print(d["KIA"])
print(d.items())
