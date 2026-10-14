from .models import Carrinho

def carrinho_total(request):
    total_items = 0
    if request.user.is_authenticated:
        carrinho = Carrinho.objects.filter(usuario=request.user).first()
        if carrinho:
            total_items = carrinho.total_items()
    return {'carrinho_total_items': total_items}