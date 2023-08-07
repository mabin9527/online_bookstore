from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import stripe
import json
from .models import StaffInfo
from utils.pagination import Pagination
from checkout.models import Order
from products.models import Product, Category
from products.forms import ProductForm




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

@login_required
def editor_add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('editor_stock_list'))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()
    userinfo = request.user
    template = 'editor/editor_add_product.html'
    context = {
        'form': form,
        'userinfo': userinfo
    }

    return render(request, template, context)

@login_required
def editor_update_product(request, pid):
    """
    Allow user to update the product details
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
            return redirect(reverse('editor_stock_list'))
        else:
            messages.error(
                request, 'Failed to update product. Check form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'editor/editor_update_product.html'
    userinfo = request.user
    context = {
        'form': form,
        'product': product,
        'categories_list': categories_list,
        'userinfo': userinfo
    }

    return render(request, template, context)

@login_required
def editor_delete_product(request, pid):
    """
    Delete product from the shop
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only Admins owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=pid)
    product.delete()
    messages.success(request, 'Product has been deleted.')

    return redirect(reverse('editor_stock_list'))

@login_required
def staff_list(request):
    """
    A view to display the employee list for the shop
    """
    employee = StaffInfo.objects.all()
    userinfo = request.user
    page_object = Pagination(request, employee)

    context = {
        'userinfo': userinfo,
        'products': page_object.page_queryset,
        'page_string': page_object.html,
        'employee': employee  
    }
    return render(request, 'editor/editor_staff_list.html', context)

