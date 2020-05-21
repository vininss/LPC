from django.http import HttpResponse, Http404
from django.urls import reverse
from django.shortcuts import render
from .models import Chamado, Funcionario, Status, Atendimento
from .forms import ChamadoForm, AtendimentoForm

from django.views.generic.edit import FormView
from django.views.generic import TemplateView

def incial(request):
    chamados = []
    if request.user.is_authenticated:
        if request.user.is_superuser:
            chamados = Chamado.objects.filter()
        
        else:
            chamados = Chamado.objects.filter(autor__usuario=request.user)
    
    else:
        return render(request, 'Solutions/erro_autenticacao.html', {})

    return render(request, 'Solutions/inicial.html', {'chamados':chamados})

def detalhes(request, id_chamado):
    if request.user.is_authenticated:
        chamado = Chamado.objects.get(pk=id_chamado)
        return render(request, 'Solutions/detalhes.html', {'chamado':chamado})
    else:
        return render(request, 'Solutions/erro_autenticacao.html', {})
        
def atendimentoGet(request):
    atendimentos = []
    if request.user.is_authenticated:
        if request.user.is_superuser:
            atendimentos = Atendimento.objects.filter()
        
        else:
            atendimentos = Atendimento.objects.filter(autor__usuario=request.user)
    
    else:
        return render(request, 'Solutions/erro_autenticacao.html', {})

    return render(request, 'Solutions/detalhes.html', {'atendimentos':atendimentos})

class ChamadoView(FormView):
    template_name = "Solutions/chamado.html"
    form_class = ChamadoForm

    def form_valid(self, form):
        dados = form.clean()
        chamado = Chamado(titulo=dados['titulo'], descricao=dados['descricao'], telefone=dados['telefone'],
        categoria=dados['categoria'],autor=Funcionario.objects.get(usuario=self.request.user),
        status=Status.objects.get(nome='Aberto'))
        chamado.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('chamado_sucesso')


class ChamadoSucessoView(TemplateView):
    template_name = "Solutions/chamado_sucesso.html"


class AtendimentoView(FormView):
    template_name = "Solutions/atendimento.html"
    form_class = AtendimentoForm
    

    def form_valid(self, form):
        dados = form.clean()
        at = Atendimento(chamado=dados['chamado'], descricao=dados['descricao'],autor=Funcionario.objects.get(usuario=self.request.user))
        dados['chamado'].status=dados['status']
        dados['chamado'].save()
        at.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('atendimento_sucesso')

class AtendimentoSucessoView(TemplateView):
    template_name = "Solutions/atendimento_sucesso.html"