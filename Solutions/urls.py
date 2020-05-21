from django.contrib import admin
from django.urls import path, include
from .views import incial,detalhes,atendimentoGet

urlpatterns = [
    path('', incial, name='inicio'),
    path('detalhes/<int:id_chamado>', detalhes, name='detalhes'),
    path('detalhes/', atendimentoGet, name='atendimentoGet'),
    
]