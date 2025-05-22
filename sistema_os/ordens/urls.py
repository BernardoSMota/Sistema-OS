from django.urls import path
from ordens.views import home

urlpatterns = [
    path('', home, name='home'),  
]