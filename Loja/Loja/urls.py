
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
   
      path('admin/', admin.site.urls),
      path('',include('home.urls')),
      path('catalogo_produtos/', include('catalogo_produtos.urls')),
      path('pesquisa/', include('pesquisa.urls')), 
       
]