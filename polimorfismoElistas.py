class Programa:
    def __init__(self, nome, diretor):
        self._nome = nome
        self._diretor = diretor
    @property
    def nome(self):
        return self._nome
    @property
    def diretor(self):
        return self._diretor

class Filme(Programa):
    def __init__(self, nome, duracao, diretor):
        self._duracao = duracao
        super().__init__(nome, diretor)
    @property
    def duracao(self):
        return self._duracao
    def __str__(self):
        return f'Nome Do Filme: {self.nome} - Duração: {self.duracao} - Diretor: {self.diretor}'


class Serie(Programa):
    def __init__(self, nome, temporadas, diretor):
        self.__temporadas = temporadas
        super().__init__(nome, diretor)
    @property
    def temporadas(self):
        return self.__temporadas
    def __str__(self):
        return f'Nome Da Serie: {self.nome} - {self.temporadas} Temporada(s)- Diretor: {self.diretor}'



TropaDeElite = Filme('Tropa De Elite', '1h 55m', 'José Padilha' )
Avatar = Filme('Avatar', ' 2h 42m ', 'James Cameron')

playlistDeFilmes = [TropaDeElite, Avatar]

TWD = Serie('The Walking Dead', '11', 'Greg Nicotero')
PB = Serie('Prision Break', '5', 'Bobby Roth' )

playlistDeSeries = [TWD, PB]

for PlayFilmes in playlistDeFilmes:
    print(PlayFilmes)
print("************")
for PlaySeries in playlistDeSeries:
    print(PlaySeries)