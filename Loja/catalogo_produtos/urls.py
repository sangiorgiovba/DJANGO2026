from django.urls import path
from . import views

app_name = 'catalogo_produtos'

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('<int:pk>/', views.detalhe_produtos, name='detalhes'),
]

