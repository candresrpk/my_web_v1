from django.urls import path
from . import views

app_name = 'carpena'


urlpatterns = [
    path('', views.index, name='home'),
]