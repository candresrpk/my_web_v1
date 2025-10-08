from django.forms import ModelForm
from .models import Categoria, Cartera, Movimiento



class CarteraForm(ModelForm):
    class Meta:
        model = Cartera
        fields = ['nombre']


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'cartera']


class MovimientoForm(ModelForm):
    class Meta:
        model = Movimiento
        fields = ['monto', 'movimiento', 'categoria', 'cartera']        
