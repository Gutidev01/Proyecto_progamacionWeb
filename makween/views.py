from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductoForm
from .models import Producto
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#Iniciar Sesion

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
            return render(request, 'makween/login.html')
    else:
        return render(request, 'makween/login.html')


#Cerrar sesión

def logout_view(request):
    logout(request)
    return redirect('index')



# Páginas.

def index(request):
    context={}
    return render(request, 'makween/index.html', context)

def mision_vision(request):
    context={}
    return render(request, 'makween/mision-vision.html', context)

def formulario(request):
    context={}
    return render(request, 'makween/formulario.html', context)

def galeria(request):
    context={}
    return render(request, 'makween/galeria.html', context)

def sucursal(request):
    context={}
    return render(request, 'makween/sucursal.html', context)

#---------------------------------------------------------------------------------------
# Productos.

    
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'makween/base.html', {'productos': productos})

def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'makween/producto_detail.html', {'producto': producto})

def producto_create(request):
    form = ProductoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        producto = form.save()
        return redirect('base')  
    return render(request, 'makween/producto_create.html', {'form': form})

def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    form = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if form.is_valid():
        producto = form.save()
        return redirect('producto_detail', pk=producto.pk)
    return render(request, 'makween/producto_update.html', {'form': form, 'producto': producto})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('base')
    return render(request, 'makween/producto_delete.html', {'producto': producto})



