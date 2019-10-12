from django import forms

class AddProductForm(forms.Form):
    name = forms.CharField(label="Nazwa produktu",max_length=50)
    description = forms.CharField(label='Opis', max_length=100)
    price = forms.FloatField(label="Podaj cenę")
    available = forms.BooleanField(label="Czy produkt jest dostępny")


