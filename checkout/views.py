from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    bag =  request.session.get('basket', {})
    if not bag:
        messages.error(
            request, "Your shopping cart is empty!")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NaPHkE0Rm3uggmIuPTlk2PAtu24YSkB3L34L9pivbw8uG3uF5y21Ioft9VIUBzNtLJeMwAlRxqEmgEIfSVsMxix00jznxU7KC',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)



