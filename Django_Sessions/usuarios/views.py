from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuarios
from django.shortcuts import redirect
from hashlib import sha256

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
        return redirect('/auth/cadastro?status=1') #Status passando que estão vazios campos email e nome
    if len(senha) < 8:
        return redirect('/auth/cadastro?status=2')#Status passando que o campo senha tem menos que 8 carct
        
    usuario = Usuarios.objects.filter(email = email)

    if len(usuario) > 0:
        return redirect('/auth/cadastro?status=3')#Ja tem alguem com esse email
    

    try:
        senha = sha256(senha.encode()).hexdigest()

        usuario = Usuarios(nome = nome, 
                        senha = senha, 
                        email = email)
        
        usuario.save()
        return redirect('/auth/login?status=0')#Cadastro concluido retorna para login
    except:
        return redirect('/auth/cadastro?status=4')#Deu erro no cadastro retorna status 4
    
def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    senha = sha256(senha.encode()).hexdigest()
    usuario = Usuarios.objects.filter(email = email).filter(senha = senha)

    if len(usuario) == 0:
        return redirect('/auth/login?status=1') #Nao encontrado usuario com esse email e senha
    elif len(usuario) > 0:
        pass