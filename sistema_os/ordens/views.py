from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'ordens/pages/index.html',
                  context={'window_title': 'Início'})


def create(request):
    return render(request, 'ordens/pages/create.html',
                  context={'window_title': 'Criando OS'})
    
    
def edit(request):
    return render(request, 'ordens/pages/edit.html',
                  context={'window_title': 'Criando OS'})