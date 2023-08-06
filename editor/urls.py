from django.urls import path
from . import views

urlpatterns = [
    path('', views.editor_index, name='editor_index'),
    path('stock/', views.editor_stock_list, name='editor_stock_list'),
    path('add/', views.editor_add_product, name='editor_add_product'),
]