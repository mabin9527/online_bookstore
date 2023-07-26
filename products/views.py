from django.shortcuts import render, get_object_or_404
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

def product_detail(request):
    """
    View to show individual product details
    """
    pid = request.GET.get('pid')
    product = get_object_or_404(Product, pk=pid)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
