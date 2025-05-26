from django.urls import path
from ordens.views import home, create, edit, verify_os

app_name = 'ordens'

urlpatterns = [
    path('', home, name='home'),  
    path('create/', create, name='create'),  
    path('edit/<int:os>/', edit, name='edit'),  
    path('verify_os/', verify_os, name='verificar_os'),
]