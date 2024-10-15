from django import forms
from ventas.models import Cliente, Producto

class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nombre', 'direccion', 'cedula_ruc', 'telefono', 'email')
        widgets = {
            'codigo': forms.TextInput(attrs={'placeholder': 'Dejar en blanco para autogenerar'}),
        }
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
            'direccion': 'Dirección',
            'cedula_ruc': 'Cédula/RUC',
            'telefono': 'Teléfono',
            'email' : 'Email',
        }

class EditarClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nombre', 'direccion', 'cedula_ruc', 'telefono', 'email')
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
            'direccion': 'Dirección',
            'cedula_ruc': 'Cédula/RUC',
            'telefono': 'Teléfono',
            'email' : 'Email',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'id': 'codigo_editar', 'placeholder': 'Dejar en blanco para autogenerar'}),
            'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'direccion': forms.TextInput(attrs={'id': 'direccion_editar'}),
            'cedula_ruc': forms.TextInput(attrs={'id': 'cedula_ruc_editar'}),
            'telefono': forms.TextInput(attrs={'id': 'telefono_editar'}),
            'email': forms.TextInput(attrs={'id': 'email_editar'}),   
        }

class AddProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo', 'descripcion', 'imagen', 'costo', 'precio',  'cantidad')

        widgets = {
            'codigo': forms.TextInput(attrs={'placeholder': 'Dejar en blanco para autogenerar'}),
        }
        labels = {
            'codigo': 'Código',
            'descripcion': 'Descipción del producto',
            'imagen': 'Imágen del producto',
            'costo': 'Costo del producto en Gs.',
            'precio' : 'Precio de venta del producto en Gs.',
            'cantidad': 'Cantidad disponible',
        }