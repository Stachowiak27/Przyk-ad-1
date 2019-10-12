
def dogs_age(age):
    if age <= 2:
        x = age * 10.5
    else:
        x = 21 + ((age-2)*4)
    return x

burek = dogs_age(1.5)
azor = dogs_age(5)

print("Wiek = ",burek,"lat")
print("Wiek = ",azor,"lat")