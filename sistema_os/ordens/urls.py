from django.urls import path
from ordens.views import home, create, edit, verify_os, edit_step, edit_step_add_pictures, edit_step_relatorio, edit_step_add_final_pictures

app_name = 'ordens'

urlpatterns = [
    path('', home, name='home'),  
    path('create/', create, name='create'),  
    path('edit/<int:os_number>/', edit, name='edit'),  
    path('edit/<int:os_number>/add_pictures', edit_step_add_pictures, name='add_pictures'),  
    path('edit/<int:os_number>/relatorio', edit_step_relatorio, name='relatorio'),  
    path('edit/<int:os_number>/final_pictures', edit_step_add_final_pictures, name='add_final_pictures'),  
    path('edit_step/', edit_step, name='edit_step'),  
    path('verify_os/', verify_os, name='verificar_os'),
]