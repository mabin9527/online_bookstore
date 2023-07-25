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

def product_detail(request):
    """
    View to show individual product details
    """
    pid = request.GET.get('pid')
    product = Product.objects.filter(pid=pid).first()
    category = Category.objects.filter(cid=product.category_id).first()
    img_list = Product.image.split('##')
    price = Product.price
    books = Product.objects.filter(category_id=product.category_id)[0:3]
    context = {
        'product': product,
        'category': category,
        'img_list': img_list,
        'price': price,
        'books': books,
    }
    return render(request, 'products/product_detail.html', context)
