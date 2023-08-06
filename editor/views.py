from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe
import json
from utils.pagination import Pagination
from checkout.models import Order
from products.models import Product



@login_required
def editor_index(request):
    """"
    A view to display editor homepage
    """
    userinfo = request.user
    context = {
        'userinfo': userinfo,
    }
    return render(request, 'editor/editor_index.html', context)

@login_required
def editor_stock_list(request):
    """"
    A view to display the total stocks
    """
    # stripe.api_key = settings.STRIPE_SECRET_KEY
    # orders = Order.objects.all()
    # for order in orders:
    #     payment_intent = stripe.PaymentIntent.retrieve(order.stripe_pid)
    products = Product.objects.all()
    userinfo = request.user
    page_object = Pagination(request, products)

    context = {
        'userinfo': userinfo,
        'products': page_object.page_queryset,
        'page_string': page_object.html
        # 'orders': orders,
        # 'payment_intent': payment_intent
        
    }
    return render(request, 'editor/editor_stock_list.html', context)


