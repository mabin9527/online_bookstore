from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.products, name='products_page'), 
    path('detail/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search_product'),
    path('add/', views.add_product, name='add_product'),
    path('edit/', views.edit_product, name='edit_product'),
    path('delete/', views.delete_product, name='delete_product'),
]
