from django.shortcuts import render
from .models import *

def product_list(request):
    try:
        products = Product.objects.all()
        context = {
            'products': products,
            'has_products': products.exists()
        }
        return render(request, 'product_list.html', context)
    except Exception as e:
        context = {
            'products': [],
            'has_products': False,
            'error_message': 'Error loading products. Please try again later.'
        }
        return render(request, 'product_list.html', context)