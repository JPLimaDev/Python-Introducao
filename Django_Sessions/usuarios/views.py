from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuarios
from django.shortcuts import redirect
from hashlib import sha256
from django.contrib import messages
from django.contrib.messages import constants
def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})
    


def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Campos email ou senha vazios')
        return redirect('/auth/cadastro') #Status passando que estão vazios campos email e nome
    if len(senha) < 8:
        messages.add_message(request, constants.ERROR, 'Senha tem que ter mais 8 caracters')
        return redirect('/auth/cadastro')#Status passando que o campo senha tem menos que 8 carct
        
    usuario = Usuarios.objects.filter(email = email)

    if len(usuario) > 0:
        messages.add_message(request , constants.ERROR, 'Email já cadastrado')
        return redirect('/auth/cadastro')#Ja tem alguem com esse email
    

    try:
        senha = sha256(senha.encode()).hexdigest()

        usuario = Usuarios(nome = nome, 
                        senha = senha, 
                        email = email)
        
        usuario.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastrado com sucesso')
        return redirect('/auth/login')#Cadastro concluido retorna para login
    except:
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
        return redirect('/auth/cadastro')#Deu erro no cadastro retorna status 4
    
def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    senha = sha256(senha.encode()).hexdigest()
    usuario = Usuarios.objects.filter(email = email).filter(senha = senha)

    if len(usuario) == 0:
        messages.add_message(request, constants.WARNING,"Usuário não encontrado")
        return redirect('/auth/login') #Nao encontrado usuario com esse email e senha
    elif len(usuario) > 0:
        request.session['logado'] = True 
        request.session['usuario_id'] = usuario[0].id
        return redirect('/plataforma/home')
    
def sair(request):
    #return HttpResponse(request.session.get_expiry_date())#Tempo de expiração da session do user
    #request.session.get_expiry_date() Data de expiração da senha
    request.session.flush()
    messages.add_message(request, constants.WARNING, 'Faça login antes de acessar a plataforma')
    return redirect('/auth/login')