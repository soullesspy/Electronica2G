from django.contrib import admin
from ventas.models import Cliente, Producto

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'direccion', 'cedula_ruc', 'telefono', 'email')
    search_fields = ['nombre']
    readonly_fields = ('create', 'update')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Cliente, ClienteAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'cantidad','codigo', 'costo')
    search_fields = ['descripcion']
    readonly_fields = ('create', 'update')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Producto, ProductoAdmin)