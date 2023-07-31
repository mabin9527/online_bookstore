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
    basket = request.session.get('basket', {})
    if pid in list(basket.keys()):
        basket[pid] += quantity
        messages.success(request, f'Updated {product.name} quantity to\{basket[pid]}')
    else:
        basket[pid] = quantity
        messages.success(request, f'Added {product.name} to your basket')
    request.session['basket'] = basket

    # redirect the current page
    return redirect(request.META['HTTP_REFERER'])

def adjust_basket(request, pid):
    """
    Update quantity of the specified product to the shopping basket
    """
    product = get_object_or_404(Product, pk=pid)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    if quantity > 0:
        basket[pid] = quantity
        messages.success(request, f'Updated {product.name} quantity to\{basket[pid]}')
    else:
        basket.pop(pid)
        messages.success(request, f'Removed {product.name} from your basket')
    
    request.session['basket'] = basket
    return redirect(reverse('view_basket'))

def remove_from_basket(request, pid):
    """Remove the item from the shopping bag"""
    try:
        product = get_object_or_404(Product, pk=pid)
        basket = request.session.get('basket', {})
        basket.pop(pid)
        print(basket)
        messages.success(request, f'Removed {product.name} from your bag')
        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
