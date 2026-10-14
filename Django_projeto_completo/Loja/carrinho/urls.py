from django.urls import path
from . import views

app_name = 'carrinho'

urlpatterns = [
    path('', views.carrinho, name='carrinho'),
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar'),
    path('deletar/<int:produto_id>/', views.deletar_del_carrinho, name='deletar'),
    path('limpar/', views.limpar_carrinho, name='limpar'),
]
