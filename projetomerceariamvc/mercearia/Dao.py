from Models import *

class daoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open("categoria.txt", "a") as arq:
            arq.writelines(f"{categoria}\n")

    @classmethod
    def ler(cls):
        with open("categoria.txt", "r") as arq:
            cls.categoria = arq.readlines()
        print(cls.categoria)

daoCategoria.salvar("Frutas")
daoCategoria.ler()