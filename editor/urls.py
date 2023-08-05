from django.urls import path
from . import views

urlpatterns = [
    path('editor/', views.editor_index, name='editor_index'),
]