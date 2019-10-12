
def calculate_net(gross,vat=1.23):
    netto = gross/vat
    return netto

print(calculate_net(100))