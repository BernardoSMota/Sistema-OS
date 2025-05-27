from django.shortcuts import render, redirect
from ordens.utils.locate_os import check_existing
from ordens.utils.create_folders import create_folder, save_imgs
from django.http import JsonResponse, Http404
from django.contrib import messages
from django.conf import settings
import os



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
        created = create_folder(request.POST, request.FILES)
        if created:
            messages.success(request, f'OS {number} criada com sucesso!')
            return redirect('ordens:home')
        
        else:
            messages.error(request, 'Algo deu errado, tente novamente')
    
    return render(request, 'ordens/pages/create.html',
                  context={'window_title': 'Criando OS'})
    
    
def edit(request, os_number):
    if request.method == 'POST':
        edits_chosen = request.POST.getlist('edit_options', [])
        
        if not edits_chosen:
            messages.error(request, 'Selecione ao menos uma etapa')
            return redirect('ordens:edit', os_number)
        
        request.session['edit_steps'] = edits_chosen
        request.session['edit_index'] = 0
        request.session['os_number'] = os_number
        
        return redirect('ordens:edit_step')

    
    return render(request, 'ordens/pages/edit.html',
                  context={'window_title': 'Criando OS',
                           'os_number': os_number})
    


def edit_step(request):
    steps = request.session.get('edit_steps', [])
    index = request.session.get('edit_index', 0)
    os_number = request.session.get('os_number')
    
    print(steps)
    
    if index >= len(steps):
        messages.success(request, f'OS {os_number} editada com sucesso')
        return redirect('ordens:home')
    
    current_step = steps[index]
    print(current_step)
    return redirect(f'ordens:{current_step}', os_number=os_number)



def edit_step_add_pictures(request, os_number):
    full_path = os.path.join(settings.CAMINHO_BASE_SALVAMENTO, str(os_number))
    save_imgs(full_path, os_number, request.FILES)
    
    return render(request, 'ordens/pages/edits/pictures.html')


def edit_step_relatorio(request, os_number):
    return render(request, 'ordens/pages/edits/relatorio.html')


def edit_step_add_final_pictures(request, os_number):
    return render(request, 'ordens/pages/edits/final_pictures.html')






def verify_os(request):
    numero_os = request.GET.get('os_number')
    existe = check_existing(numero_os)
    return JsonResponse({'existe': existe})