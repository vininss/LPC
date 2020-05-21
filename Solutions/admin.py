from django.contrib import admin

from .models import Status, Funcionario, Categoria, Chamado, Atendimento

admin.site.register(Status)
admin.site.register(Funcionario)
admin.site.register(Categoria)
admin.site.register(Chamado)
admin.site.register(Atendimento)
