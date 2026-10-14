from django.shortcuts import render, get_object_or_404
from catalogo_produtos.models import Produto
from django.core.paginator import Paginator


def lista_produtos(request):
    Produtos = Produto.objects.all().order_by('id')

    paginator = Paginator(Produtos, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    contexto_lista_produtos = {
        'lista_produtos': page_obj
    }

    return render(
        request,
        'catalogo_produtos/lista_produtos.html',
        contexto_lista_produtos
    )


def detalhe_produtos(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    context = {'produto': produto}

    return render(
        request,
        'catalogo_produtos/detalhes.html',
        context
    )
