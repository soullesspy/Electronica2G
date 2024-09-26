from django import forms
from ventas.models import Cliente

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
        fields = ('codigo', 'nombre','telefono')
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
            'telefono': 'Teléfono',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}),
            'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'telefono': forms.TextInput(attrs={'id': 'telefono_editar'}),
        }