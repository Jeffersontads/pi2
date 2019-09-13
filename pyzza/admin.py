from django.contrib import admin

# Register your models here.
from pyzza.models import TipoPizza, Ingrediente, SaborBorda, TamanhoPizza, SaborPizza, TamanhoBebida, Bebida, \
    Entregador, Cliente, StatusPedido, FormaDePagamento, BebidaTamanhoBebida, SaborPizzaIngrediente

admin.site.register(TipoPizza)
admin.site.register(Ingrediente)
admin.site.register(SaborBorda)

class IngredienteInLine(admin.TabularInline):
    model = SaborPizzaIngrediente
    extra = 0

class SaborPizzaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['id', 'tipo_pizza', 'nome', 'valor_adicional']
    list_display_links = ['id', 'tipo_pizza', 'nome', 'valor_adicional']
    ordering = ['nome']
    inlines = [IngredienteInLine]
admin.site.register(SaborPizza, SaborPizzaAdmin)

admin.site.register(TamanhoPizza)
admin.site.register(TamanhoBebida)

class TamanhoBebidaInLine(admin.TabularInline):
    model = BebidaTamanhoBebida
    extra = 0

class BebidaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['id', 'nome']
    list_display_links = ['id', 'nome']
    ordering = ['nome']
    inlines = [TamanhoBebidaInLine]

admin.site.register(Bebida, BebidaAdmin)
admin.site.register(Entregador)

# class PaisAdmin(admin.ModelAdmin):
#     search_fields = ['nome']
#     inlines = [EstadoAdminInline]
#     list_display = ['id','nome']
#     list_editable = ['nome']
#     ordering = ['nome']
admin.site.register(Cliente)

admin.site.register(StatusPedido)
admin.site.register(FormaDePagamento)


