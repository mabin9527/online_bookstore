from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from django.contrib.auth.decorators import login_required
from .models import Product, Category
from .forms import ProductForm


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
    pid = request.GET['pid']
    product = get_object_or_404(Product, pk=pid)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)

def search(request):
    """
    Users are allowed to search specific products in store
    """
    products = Product.objects.all()
    categories_list = Category.objects.all()
    book_info = None
    category = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            if sort_key == 'category':
                sort_key = 'category__name'
            if sort_key == 'name':
                sort_key = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_key = f'-{sort_key}'
            products = products.order_by(sort_key)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
    
    if request.GET:
        if 'q' in request.GET:
            book_info = request.GET['q']
            if not book_info:
                messages.error(request, 'Please enter search criteria!')
                return HttpResponseRedirect('/products')
    
            queries = Q(name__icontains=book_info) | Q(
                author__icontains=book_info) | Q(
                description__icontains=book_info)
            products = products.filter(queries)

    current_sort = f'{sort}_{direction}'

    context = {
        'search_term': book_info,
        'categories_list': categories_list,
        'current_sort': current_sort,
        'products': products,
    }     
    return render(request, 'products/search_product.html', context)   





