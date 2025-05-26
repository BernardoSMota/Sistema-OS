from django.urls import path
from ordens.views import home, create, edit

app_name = 'ordens'

urlpatterns = [
    path('', home, name='home'),  
    path('create/', create, name='create'),  
    path('edit/', edit, name='edit'),  
    
]