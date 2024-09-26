from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cliente, Producto
from .forms import AddClienteForm

# Create your views here.

def ventas_view(request):
    return render(request, 'ventas.html')

def clientes_view(request):
    clientes = Cliente.objects.all()
    form_personal = AddClienteForm()
    context = {
        'clientes' : clientes,
        'form_personal' : form_personal
    }
    return render(request, 'clientes.html', context)

def add_cliente_view(request):
    #print("guardar clientes")
    if request.POST:
        form = AddClienteForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
                messages.success(request, "Cliente guardado exitosamente")
            except:
                messages.error(request, "Error al guardar el cliente")
                return redirect('Clientes')
    return redirect('Clientes')

def edit_cliente_view(request):
    return redirect('Clientes')

def delete_cliente_view(request):
    return redirect('Clientes')