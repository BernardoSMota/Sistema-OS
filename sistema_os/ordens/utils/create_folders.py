from django.conf import settings
from datetime import datetime
import os
from decouple import config


def create_folder(post, files):
    os_details = {
            'number': post.get('os-number'),
            'client': post.get('client'),
            'equipment': post.get('equipment'),
            'brand': post.get('brand'),
            'pot': post.get('pot'),
            'rotation': post.get('rotation'),
            'pictures': post.get('pictures'),
        }
    

    full_path = os.path.join(settings.CAMINHO_BASE_SALVAMENTO, os_details['number'])
    os.makedirs(full_path, exist_ok=True)
    
    create_txt(full_path, os_details['number'], os_details['client'], os_details['equipment'], os_details['brand'], os_details['pot'], os_details['rotation'])
    
    if files:
        save_imgs(full_path, os_details['number'], files)
    
    return True   

        
def save_imgs(path, os_number, files):
    images = files.getlist('pictures')
    image_folder_name = config('IMAGENS')
    image_folder_path = os.path.join(path, image_folder_name)
    os.makedirs(image_folder_path, exist_ok=True)
    
    num_to_sum = 0 if len(os.listdir(image_folder_path)) == 0 else len(os.listdir(image_folder_path))
    
    for num,img in enumerate(images):
        ext = os.path.splitext(img.name)[1]
        nome_arquivo = f'OS {os_number} - {(num + num_to_sum + 1):03}{ext}'
        full_path = os.path.join(image_folder_path, nome_arquivo)

        with open(full_path, 'wb+') as file:
            for chunk in img.chunks():
                file.write(chunk)
        

def create_txt(path, os_number, client, equip, brand, pot, rotation):
    txt_path = os.path.join(path, '99 - Info. da OS.txt')
    txt = f'''Número da OS: {os_number}
Cliente: {client}
Equipamento: {equip}
Marca: {brand}
Potência: {pot}
RPM: {rotation}
Criação: {datetime.now()}
'''

    with open(txt_path, 'w', encoding='utf-8') as file:
        file.write(txt)
   