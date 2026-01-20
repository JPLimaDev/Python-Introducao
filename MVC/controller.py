#Responsável pela logica controller
from dao import PessoaDao
from model import Pessoa
class PessoaController:
    @classmethod
    def cadastrar(cls, nome, idade, cpf):
        if len(nome) > 2 and (idade > 0 and idade < 200) and len(cpf) == 14:
            try :
                p = Pessoa(nome, idade, cpf)
                PessoaDao.salvar(p)
                return True
            except:
                return False
        else:
            return False 
        

