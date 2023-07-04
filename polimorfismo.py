class Programacao:
    def __init__(self, nome):
        self._nome = nome
        self._likes = 0
    @property
    def nome(self):
        return self._nome
    @property
    def likes(self):
        return self._likes
    def dar_likes(self):
        self._likes += 1

class Filme(Programacao):
    def __init__(self, nome, duracao):
        super().__init__(nome)
        self._duracao = duracao
    @property
    def duracao(self):
        return self._duracao

class Serie(Programacao):
    def __init__(self, nome, temporadas):
        super().__init__(nome)
        self._temporadas = temporadas
    @property
    def temporadas(self):
        return self._temporadas



Guerra_dos_mundos = Filme('Guerra Dos Mundos 1', '1h 56m' )
Guerra_dos_mundos.dar_likes()


TWD = Serie('The Walking Dead', 11)
TWD.dar_likes()


print('---------------------------------------')
Conteudo_FOX = [Guerra_dos_mundos, TWD]

for conteudo in Conteudo_FOX:
    detalhes = conteudo.temporadas if hasattr(conteudo, 'temporadas') else conteudo.duracao
    print('Nome: {}, Likes: {}, Detalhes: {}'.format(conteudo.nome, conteudo.likes, detalhes))