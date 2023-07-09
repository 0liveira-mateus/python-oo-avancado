class Programas:
    def __init__(self, nome, lancamento, diretor):
        self._nome = nome
        self._lancamento = lancamento
        self._diretor = diretor
    @property
    def nome(self):
        return self._nome
    @property
    def lancamento(self):
        return self._lancamento
    @property
    def diretor(self):
        return self._diretor
class Filmes(Programas):
    def __init__(self, nome, lancamento, duracao):
        super().__init__(nome, lancamento, 0)
        self._duracao = duracao
    @property
    def duracao(self):
        return self._duracao
    def __str__(self):
        return f'O filme {self.nome}, lançado(a) em {self.lancamento} tem duração de {self.duracao}'
class Series(Programas):
    def __init__(self, nome, lancamento, temporadas):
        super().__init__(nome, lancamento, 0)
        self.__temporadas = temporadas
    @property
    def temporadas(self):
        return self.__temporadas
    def __str__(self):
        return f'A serie {self.nome}, lançado(a) em {self.lancamento} tem {self.temporadas} temporadas'

Vingadores = Filmes('Guerra Infinta', 2018, '2h30m')

TWD = Series('The Walking Dead', 2010, 11)

Playlist = [Vingadores, TWD]

for Dados in Playlist:
    print(Dados)