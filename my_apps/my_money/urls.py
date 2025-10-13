from django.urls import path
from . import views

app_name = 'my_money'


urlpatterns = [
    path('', views.HomeView, name='home'),
    path('dashboard/', views.My_money_dashboardView, name='dashboard'),
    path('create_cartera/', views.CreateCarteraView, name='create_cartera'),
]