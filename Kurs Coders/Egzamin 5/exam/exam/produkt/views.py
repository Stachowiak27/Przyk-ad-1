from django.views import View
from django.shortcuts import render
from .models import Product, Category
from .forms import AddProductForm




class ExamView(View):

    def get(self, request):
        products = Product.objects.all()
        return render(request, 'products.html', {'products': products})


class ProductView(View):


    def get(self, request, id):
        product = Product.objects.get(id=id)
        categories = Category.objects.all()
        return render(request, 'product.html', {'product': product, 'categories': categories})

class AddProductView(View):
    def get(self,request):
        form = AddProductForm()
        return render(request, "add_product.html", {'form':form})

    def post(self,request):
        form = AddProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                price = form.cleaned_data['price'],
                available = form.cleaned_data['available']
            )
        return render(request,'add_product.html', {'form': form})