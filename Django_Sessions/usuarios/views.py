from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from hashlib import sha256
from django.contrib import messages, auth
from django.contrib.messages import constants
from django.contrib.auth.models import User

def login(request):
    if request.user.is_authenticated:
        return redirect('/plataforma/home')
    
    return render(request, 'login.html')


def cadastro(request):
    return render(request, 'cadastro.html')
    


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
        

    if User.objects.filter(email = email).exists():
        messages.add_message(request , constants.ERROR, 'Existe Email já cadastrado')
        return redirect('/auth/cadastro')#Ja tem alguem com esse email
    
    if User.objects.filter(username = nome).exists():
        messages.add_message(request , constants.ERROR, 'Existe Email Nome já cadastrado')
        return redirect('/auth/cadastro')#Ja tem usuario com esse nome
    try:
        
        usuario = User.objects.create_user(username = nome, email = email, password=senha)
        
        usuario.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastrado com sucesso')
        return redirect('/auth/login')#Cadastro concluido retorna para login
    except:
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
        return redirect('/auth/cadastro')#Deu erro no cadastro retorna status 4
    
def valida_login(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    
    usuario = auth.authenticate(request , username = nome, password = senha)
    print(usuario)
    if not usuario:
        messages.add_message(request, constants.WARNING,"Email ou Senha inválido")
        return redirect('/auth/login') #Nao encontrado usuario com esse email e senha
    else:
        auth.login(request, usuario)
        return redirect('/plataforma/home')
    
def sair(request):
    #return HttpResponse(request.session.get_expiry_date())#Tempo de expiração da session do user
    #request.session.get_expiry_date() Data de expiração da senha
    #request.session.flush()
    #messages.add_message(request, constants.WARNING, 'Faça login antes de acessar a plataforma')
    auth.logout(request)
    return redirect('/auth/login')