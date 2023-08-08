from django.urls import path
from . import views

urlpatterns = [
    path('', views.editor_index, name='editor_index'),
    path('stock/', views.editor_stock_list, name='editor_stock_list'),
    path('add/', views.editor_add_product, name='editor_add_product'),
    path('update/<int:pid>/', views.editor_update_product, name='editor_update_product'),
    path('delete/<int:pid>/', views.editor_delete_product,name='editor_delete_product'),
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/<int:id>/update', views.staff_update_details, name='staff_update_details'),
    path('staff/<int:id>/delete', views.staff_delete, name='staff_delete'),
    path('staff/add', views.staff_add, name='staff_add'),
]