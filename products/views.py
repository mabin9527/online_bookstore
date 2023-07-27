from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

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

def search(request):
    if request.method == "GET":
        book_info = request.GET.get('book_info')
        if not book_info:
            messages.error(request, 'Please enter search criteria!')
            return redirect(reverse('products'))
        books = Product.objects.filter(name_icontains=book_info, 
        author_icontains=book_info, description_icontains=book_info)
        context = {
            'books': books
        }     
        return render(request, 'products', context)   

# @login_required
# def add_to_cart(request):
#     """
#     Add selected product to the shopping bag
#     """
#     if request.method == "POST":
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save()
#             messages.success(request, 'The item has been successfully added to your basket!')
#             return redirect(reverse('product_detail', args=[product.id]))
#         else:
#             messages.error(request, 'Failed to add product. Please check form is valid.')
#     else:
#         form = ProductForm()
    
#     template = 'products/add_product.html'
#     context = {
#         'form': form,
#     }
#     return render(request, template, context)
