from django.urls import path
from . import views

app_name = 'my_money'


urlpatterns = [
    path('', views.HomeView, name='home'),
]