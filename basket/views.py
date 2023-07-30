from django.contrib import messages
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from products.models import Product, Category


def view_basket(request):
    """
    A view to display the basket page
    """
    product = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'product': product,
        'categories': categories
    }
    return render(request, 'basket/basket.html', context)

def add_to_basket(request, pid):
    """
    A view to add a quantity of the specified product to the shopping basket
    """
    product = get_object_or_404(Product, pk=pid)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    if pid in list(basket.keys()):
        basket[pid] += quantity
        messages.success(request, f'Updated {product.name} quantity to\{basket[pid]}')
    else:
        basket[pid] = quantity
        messages.success(request, f'Added {product.name} to your basket')
    request.session['basket'] = basket
    return redirect(redirect_url)
