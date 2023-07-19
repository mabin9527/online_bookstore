from django.urls import path, re_path
from . import views

urlpatterns = [
    path('products/', views.products, name='products'), 

]
app_name = 'products'