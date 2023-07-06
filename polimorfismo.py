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

    def __str__(self):
        return 'Nome do Filme: {}, Duração : {} '.format(self.nome, self.duracao)

class Serie(Programacao):
    def __init__(self, nome, temporadas):
        super().__init__(nome)
        self._temporadas = temporadas
    @property
    def temporadas(self):
        return self._temporadas
    def __str__(self):
        return 'Nome da Serie: {}, Temporadas : {} '.format(self.nome, self.temporadas)

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas
    def listagem(self):
        return self.programas
    def tamanho(self):
        return len(self.programas)



Guerra_dos_mundos = Filme('Guerra Dos Mundos 1', '1h 56m' )
TWD = Serie('The Walking Dead', 11)
Avatar = Filme('Avatar', '2h 6m' )
PrisionBreak = Serie('Prision Break', '3' )


Guerra_dos_mundos.dar_likes()
TWD.dar_likes()
Avatar.dar_likes()
PrisionBreak.dar_likes()


playlist_fim_de_semana = Playlist('Playlist para o fim de semana', [Guerra_dos_mundos, TWD,PrisionBreak, Avatar])



print('---------------------------------------')

for programacao in playlist_fim_de_semana.programas:
    print(programacao)
