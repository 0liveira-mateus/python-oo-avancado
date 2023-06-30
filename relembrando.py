class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    @property
    def like(self):
        return self._likes
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    def dar_likes(self):
        self._likes = + 1

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas




vingadores = Filme('Vingadores Ultimato', 2018, '2 horas')
vingadores.dar_likes()
print('Filme: Nome: {}, ano: {}, duração: {}, likes: {}'.format(vingadores.nome, vingadores.ano, vingadores.duracao, vingadores.like))
#----------------------------------------------------------------------------------------------------------------------
atlanta = Serie('atlanta', 2020, 2)
atlanta.dar_likes()
print('Série: Nome: {}, ano: {}, temporadas: {}, likes: {}'.format(atlanta.nome, atlanta.ano, atlanta.temporadas, atlanta.like))


