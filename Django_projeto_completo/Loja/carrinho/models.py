from django.db import models
from django.conf import settings
from catalogo_produtos.models import Produto

class Carrinho(models.Model):
    
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='carrinho'
    )
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Carrinho de compras {self.usuario.username}"

    def total_items(self):
        
        return sum(item.quantidade for item in self.items.all())

    def total_preco(self):
        
        return sum(item.subtotal() for item in self.items.all())


class ItemCarrinho(models.Model):
    
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='items')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('carrinho', 'produto')

    def __str__(self):
        return f"{self.produto.nome} x {self.quantidade}"

    def subtotal(self):
        
        return self.produto.preco * self.quantidade