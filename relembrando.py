class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0
    @property
    def like(self):
        return self.__likes
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    def dar_likes(self):
        self.__likes = + 1

vingadores = Filme('Vingadores Ultimato', 2018, '2 horas')

vingadores.dar_likes()
print('Filme: Nome: {}, ano: {}, duração: {}, likes: {}'.format(vingadores.nome, vingadores.ano, vingadores.duracao, vingadores.like))

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0
    @property
    def like(self):
        return self.likes
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    def dar_likes(self):
        self.likes = + 1



atlanta = Serie('atlanta', 2020, 2)
atlanta.dar_likes()
print('Série: Nome: {}, ano: {}, temporadas: {}, likes: {}'.format(atlanta.nome, atlanta.ano, atlanta.temporadas, atlanta.likes))


