from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from catalogo_produtos.models import Produto
from .models import Carrinho, ItemCarrinho



@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)

    item, criar = ItemCarrinho.objects.get_or_create(
        carrinho=carrinho,
        produto=produto
    )

    if not criar:
        item.quantidade += 1
        messages.info(
            request,
            f"Mais uma unidade de '{produto.nome}' foi adicionada ao carrinho."
        )
    else:
        messages.success(
            request,
            f"'{produto.nome}' foi adicionado ao carrinho com sucesso!"
        )

    item.save()

    return redirect('catalogo_produtos:detalhes', pk=produto_id)


@login_required
def deletar_del_carrinho(request, produto_id):
    carrinho, _ = Carrinho.objects.get_or_create(
        usuario=request.user
    )

    item = carrinho.items.filter(
        produto_id=produto_id
    ).first()

    if item:
        nome_produto = item.produto.nome
        item.delete()

        messages.warning(
            request,
            f"Produto '{nome_produto}' deletado do carrinho."
        )
    else:
        messages.error(
            request,
            "Não há esse produto no carrinho."
        )

    return redirect('carrinho:carrinho')


@login_required
def limpar_carrinho(request):
    carrinho, _ = Carrinho.objects.get_or_create(
        usuario=request.user
    )

    if carrinho.items.exists():
        carrinho.items.all().delete()

        messages.warning(
            request,
            "Todos os produtos foram excluídos do carrinho."
        )
    else:
        messages.info(
            request,
            "O carrinho já estava vazio."
        )

    return redirect('carrinho:carrinho')


@login_required
def carrinho(request):
    carrinho, _ = Carrinho.objects.get_or_create(
        usuario=request.user
    )

    items = carrinho.items.select_related('produto')

    total = carrinho.total_preco()

    return render(
        request,
        'carrinho/carrinho.html',
        {
            'carrinho': carrinho,
            'items': items,
            'total': total,
        }
    )
