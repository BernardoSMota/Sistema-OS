from django.shortcuts import render, redirect
from ordens.utils.locate_os import check_existing
from ordens.utils.create_folders import create_folder
from django.http import JsonResponse
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == 'POST':
        os_number = request.POST.get('os-number')
        if check_existing(os_number):
            return(redirect('ordens:edit', os_number))
        else:
            messages.warning(request, f'OS {os_number} não existe')            
            
                
    return render(request, 'ordens/pages/index.html',
                  context={'window_title': 'Início',})
    


def create(request):
    if request.method == 'POST':
        number = request.POST.get('os-number')
        created = create_folder(request.POST)
        if created:
            messages.success(request, f'OS {number} criada com sucesso!')
            return redirect('ordens:home')
        
        else:
            messages.error(request, 'Algo deu errado, tente novamente')
    
    return render(request, 'ordens/pages/create.html',
                  context={'window_title': 'Criando OS'})
    
    
def edit(request, os):
    return render(request, 'ordens/pages/edit.html',
                  context={'window_title': 'Criando OS',
                           'os_number': os})
    
    

def verify_os(request):
    numero_os = request.GET.get('os_number')
    existe = check_existing(numero_os)
    return JsonResponse({'existe': existe})