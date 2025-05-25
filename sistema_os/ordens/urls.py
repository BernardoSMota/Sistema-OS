from django.urls import path
from ordens.views import home, create

app_name = 'ordens'

urlpatterns = [
    path('', home, name='home'),  
    path('create/', create, name='create'),  
]