import os
from django.conf import settings


def check_existing(number):
    LOCAL = settings.CAMINHO_BASE_SALVAMENTO
    for nome_pasta in os.listdir(LOCAL):
        if nome_pasta == number:
            return True
    return False
    