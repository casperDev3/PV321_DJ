from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    # return RESTful response
    return render(request, 'product_list.html', {'products': products}, content_type='application/json')

