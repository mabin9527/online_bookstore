from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe
import json
from checkout.models import Order



@login_required
def editor_index(request):
    """"
    A view to display editor homepage, containing order list from customers
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    orders = Order.objects.all()
    for order in orders:
        payment_intent = stripe.PaymentIntent.retrieve(order.stripe_pid)

    userinfo = request.user
    context = {
        'userinfo': userinfo,
        'orders': orders,
        'payment_intent': payment_intent
    }
    return render(request, 'editor/editor_index.html', context)


