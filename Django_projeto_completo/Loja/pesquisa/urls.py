from django.urls import path
from . import views

app_name = 'pesquisa'

urlpatterns = [
    path('', views.pesquisa_Produtos, name='pesquisa_produtos'),
]
