from model import categoria
from dal import categoriaDal
class categoriaController:
    @classmethod
    def cadastrar_categoria(cls, id, nome, descricao):
        if len(nome) > 3:
            try:
                nova_categoria = Categoria(id, nome, descricao)
                categoriaDal.salvar_categoria(nova_categoria)
                return "Categoria cadastrada"
            
            except 