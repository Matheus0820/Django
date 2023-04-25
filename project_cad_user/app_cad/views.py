from django.shortcuts import render
from .models import Usuario


def page(request):
    return render(request, 'usuarios/page.html')


def user(request):
    novo_usuario = Usuario()
    # Salvando dados no banco de dados
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    # Exibição de dados para o usuário
    users1 = {
        'users': Usuario.objects.all()
    }

    # Mandando o dado para a página de listagem
    return render(request, 'usuarios/users.html', users1)
