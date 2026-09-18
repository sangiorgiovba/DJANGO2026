from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6,decimal_places=2)
    detalhes = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200,default="default.png")

    def __str__(self):
        return self.nome
    

