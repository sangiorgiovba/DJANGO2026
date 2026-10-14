from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contato/', views.contato, name='contato'),
]