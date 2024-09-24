from django.contrib import admin
from ventas.models import Cliente, Producto

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono','codigo', 'cedula_ruc')
    search_fields = ['nombre']
    readonly_fields = ('create', 'update')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Cliente, ClienteAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'cantidad','codigo', 'costo')
    search_fields = ['nombre_producto']
    readonly_fields = ('create', 'update')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Producto, ProductoAdmin)