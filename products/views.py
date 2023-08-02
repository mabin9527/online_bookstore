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

def product_detail(request, pid):
    """
    View to show individual product details
    """
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
        'products': products,
        'search_term': book_info,
        'categories_list': categories_list,
        'current_sort': current_sort
    }     
    return render(request, 'products/search_product.html', context)   

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('products_page'))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, pid):
    """
    Edit product in the store
    """

    categories_list = Category.objects.all()

    if not request.user.is_superuser:
        messages.error(request, 'Only Admins can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=pid)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product has been updated.')
            return redirect(reverse('products_page'))
        else:
            messages.error(
                request, 'Failed to update product. Check form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'categories_list': categories_list,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products_page'))
