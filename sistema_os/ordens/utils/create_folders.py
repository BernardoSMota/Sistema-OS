from django.conf import settings
from datetime import datetime
import os


def create_folder(post, first=False):
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
    
    if first:
        create_txt(full_path, os_details['number'], os_details['client'], os_details['equipment'], os_details['brand'], os_details['pot'], os_details['rotation'])
    
    return True
        
        
def create_txt(caminho, os_number, client, equip, brand, pot, rotation):
    txt = os.path.join(caminho, '99 - Info. da OS.txt')
    with open(txt, 'w', encoding='utf-8') as file:
        file.write(
            f'''Número da OS: {os_number}
Cliente: {client}
Equipamento: {equip}
Marca: {brand}
Potência: {pot}
RPM: {rotation}
Criação: {datetime.now()}
'''
)