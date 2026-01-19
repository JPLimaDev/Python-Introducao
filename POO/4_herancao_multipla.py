class Animal:
    def andar(self):
        print('Estou andando...')

    def correr(self):
        print('Estou correndo...')

    def pular(self):
        print('Estou pulando...')


class Felino():
    def felino(self):
        print('Sou um felino...')
    def andar(self):
        print('O felino está andando...')

class Gato(Felino, Animal):
    def miar(self):
        print('O gato está miando...')


class Cachorro(Animal):
    def latir(self):
        print('Au Au!')


y = Gato()
y.andar()