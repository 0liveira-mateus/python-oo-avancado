class Programacao:
    def __init__(self, nome, ano_lancamento):
        self.__nome = nome
        self.__ano = ano_lancamento

    @property
    def nome(self):
        return self.__nome

    @property
    def ano(self):
        return self.__ano

class Filme(Programacao):
    def __init__(self, nome, ano_lancamento, duracao):
        super().__init__(nome, ano_lancamento)
        self.__duracao = duracao
    @property
    def duracao(self):
        return self.__duracao
    def __str__(self):
        return f'Nome:{self.nome} - Ano De Lançamento: {self.ano}'

class Serie(Programacao):
    def __init__(self, nome, ano_lancamento, temporadas):
        super().__init__(nome, ano_lancamento)
        self.__temporadas = temporadas
    @property
    def temporadas(self):
        return self.__temporadas

class Playlist:
    def __init__(self, nome, programas):
        self.__nome = nome
        self.__programas = programas

    def __getitem__(self, item):
        return self.__programas[item]

    def listagem(self):
        return self.__programas

    def __len__(self):
        return len(self.__programas)


Vingadores = Filme('Guerra infinita', 2018, '1h40m')
Avatar_2 = Filme('Avatar 2', 2018, '2h50m')

Lista1 = [Vingadores, Avatar_2]
Fim_De_Semana = Playlist('Fim de Semana', Lista1)

print(f'Tamanho da Lista: {len(Fim_De_Semana.listagem())}')

for Filmes in Fim_De_Semana:
    print(Filmes)
