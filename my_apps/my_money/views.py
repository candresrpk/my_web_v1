from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CarteraForm, CategoriaForm, MovimientoForm

# Create your views here.


def HomeView(request):
    
    if request.user.is_authenticated:
        return redirect('my_money:dashboard')
    else:
        messages.info(request, 'Por favor, inicia sesión para continuar a la aplicación My Money')
        return redirect('accounts:login')
    

def My_money_dashboardView(request):
    return render(request, 'my_money/my_money_dashboard.html')


def CreateCarteraView(request):
    
    usuario = request.user
    if request.method == 'POST':
        form = CarteraForm(request.POST)
        if form.is_valid():
            cartera = form.save(commit=False)
            cartera.usuario = usuario
            cartera.save()
            return render(request, 'my_money/home.html')
    else:
        form = CarteraForm()
        context = {'form': form}
        return render(request, 'my_money/create_cartera.html', context)
    
    return render(request, 'my_money/create_cartera.html')    



