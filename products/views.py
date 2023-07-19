from django.shortcuts import render


from django.shortcuts import render
from .models import Product, Category

def products(request):
    """
    A view to show the main page of bookstore, including book categorys,
    products and search queries
    """
    categorys = Category.objects.all()
    books = Product.objects.filter().all()
    context = {
        'categorys': categorys,
        'books': books
    }
    return render(request, 'products/products.html', context)
