from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Category, Phone


# Create your views here.


def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)


def get_products(request, pk):
    products = Phone.objects.filter(category=pk)
    context = {
        'products': products
    }
    return render(request, 'products.html', context=context)


def detail(request, pk):
    product = Phone.objects.get(pk=pk)
    context = {
        'product': product
    }
    print(1)
    return render(request, 'detail.html', context=context)
