from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.products, name='products_page'), 
    path('detail/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search_product'),
]
