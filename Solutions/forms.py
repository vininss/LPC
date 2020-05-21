from django import forms
from .models import Categoria, Funcionario, Status, Chamado
from django.contrib.auth.models import User

class ChamadoForm(forms.Form):
    titulo = forms.CharField(max_length=128)    
    descricao = forms.CharField(widget=forms.Textarea)
    telefone = forms.CharField(max_length=20)    
    categoria = forms.ModelChoiceField(queryset=Categoria.objects)
    
    def clean(self):
        dados = super().clean()
        return dados

class AtendimentoForm(forms.Form):
    chamado = forms.ModelChoiceField(queryset=Chamado.objects)   
    descricao = forms.CharField(widget=forms.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects)
    
    def clean(self):
        dados = super().clean()
        return dados