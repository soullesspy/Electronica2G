from django.shortcuts import render

# Create your views here.

def ventas_view(request):
    return render(request, 'ventas.html')
