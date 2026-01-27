from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    pessoa = [{'nome': 'caio', 'idade': 20, 'profissao': 'programador'}, 
              {'nome': 'joao', 'idade': 30, 'profissao': 'dev'}]
    
    return render(request, 'cadastro/index.html', {'pessoa':pessoa , 'x': 0} )


