from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for pid, item_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=pid)
            total += item_data * product.price
            product_count += item_data
            basket_items.append({
                'pid': pid,
                'quantity': item_data,
                'product': product,
            })
    
    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
    }

    return context