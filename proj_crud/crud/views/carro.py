from django.shortcuts import render, get_object_or_404
from crud.models import Carro


def listar_carros(request):
    carros = Carro.objects.all()
    context = {
        'carros': carros,
    }
    return render(request, 'crud/listar_carros.html', context)

def deletar_carro(request, carro_id):
    carro = get_object_or_404(Carro, pk=carro_id) #vai tentar deletar se não vai abrir a página 404
    
    try:
        carro.delete()
        context = {
            'message':"Carro deletado com sucesso!",
        }
        return render(request, 'crud/listar_carros.html', context)
    except:
        context = {
            'message':"Erro ao deletar o carro!"
        }
        return render(request, 'crud/listar_carros.html', context)