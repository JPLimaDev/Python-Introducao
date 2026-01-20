from model import Categoria
class categoriaDal:
    def __init__(self):
        self.categorias = []

    @classmethod
    def salvar_categoria(self, categoria: Categoria):
        self.categorias.append(categoria)