from django.shortcuts import render
from .forms import CarteraForm, CategoriaForm, MovimientoForm

# Create your views here.


def HomeView(request):
    return render(request, 'my_money/home.html')


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



