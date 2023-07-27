from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category
from django.contrib import messages
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
    pid = request.GET.get('pid')
    product = get_object_or_404(Product, pk=pid)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)

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
