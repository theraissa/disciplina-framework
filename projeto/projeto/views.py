from django.shortcuts import render

def index(request):
    context = {
        "nome":"Raissa Maciel Lima"     
    }
    return render(request, 'home.html', context)


