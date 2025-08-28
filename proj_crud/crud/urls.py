
from django.urls import path
from . import views

app_name = 'crud' 

urlpatterns = [
    path('carros/', views.listar_carros, name='listar_carros'),
    path('crud/deletar/<int:carro_id>', views.deletar_carro, name='deletar_carro'),
]
