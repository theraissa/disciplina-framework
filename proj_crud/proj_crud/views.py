from django.shortcuts import render

def home(request):
    context = {
        'nome': "Victor"
    }
    return render(request, 'conteudo.html', context)
