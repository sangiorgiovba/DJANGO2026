from django.shortcuts import render
from catalogo_produtos.models import Produto
from django.core.paginator import Paginator
from django.db.models import Q


def pesquisa_Produtos(request):
    query = request.GET.get('q','')
    results = Produto.objects.filter(
        Q(nome__icontains=query) | Q(detalhes__icontains=query)).order_by('id')

    paginator = Paginator(results,6)
    page_number= request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'query':query,
        'lista_produtos':page_obj
    }
    return render(request,'pesquisa/results_pesquisa.html',context)

    