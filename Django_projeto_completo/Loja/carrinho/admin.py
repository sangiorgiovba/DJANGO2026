from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Carrinho, ItemCarrinho


class ItemCarrinhoInline(admin.TabularInline):
    model = ItemCarrinho
    extra = 0
    readonly_fields = ('subtotal',)


@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'criado', 'atualizado', 'total_de_itens', 'valor_total')
    search_fields = ('usuario__username', 'usuario__email')
    readonly_fields = ('criado', 'atualizado')
    inlines = [ItemCarrinhoInline]

    def total_de_itens(self, obj):
        return obj.total_items()

    total_de_itens.short_description = 'Quantidade'

    def valor_total(self, obj):
        return obj.total_preco()

    valor_total.short_description = 'Valor total'


@admin.register(ItemCarrinho)
class ItemCarrinhoAdmin(admin.ModelAdmin):
    list_display = ('carrinho', 'produto', 'quantidade', 'subtotal_produto')
    search_fields = (
        'carrinho__usuario__username',
        'produto__nome',
    )
    list_filter = ('produto',)

    def subtotal_produto(self, obj):
        return obj.subtotal()

    subtotal_produto.short_description = 'Subtotal'
