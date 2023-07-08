class Animal:
    def __init__(self, nome, peso, idade, patas, cor_pelo):
        self._nome = nome
        self._peso = peso
        self._idade = idade
        self._patas = patas
        self._cor = cor_pelo

    @property
    def qtnd_patas(self):
        return self._patas
    @property
    def nome(self):
        return self._nome
    @property
    def peso(self):
        return self._peso
    @property
    def idade(self):
        return self._idade
    @property
    def cor(self):
        return self._cor


class Mamifero(Animal):
    def __init__(self, nome, peso, idade, patas, cor_pelo):
        super().__init__(nome, peso, idade, patas, cor_pelo)

    def __str__(self):
        if self._patas == 0:
            return f'O animal não tem patas'
        else:
            return f'O Mamifero {self.nome}, possui {self.peso} kg, tem {self.idade} anos de idade, {self.qtnd_patas} patas e cor de pelos {self._cor}'

class Aquaticos(Animal):
    def __init__(self, nome, peso, idade, predador, nada):
        super().__init__(nome, peso, idade, 0, 0)
        self._predador = predador
        self._nada = nada
    @property
    def predador(self):
        if self._predador == 'sim':
            return f' O animal {self.nome} é um predador'
        else:
            return f' O animal {self.nome} Não é um predador'
    @property
    def nada(self):
        if self._nada == 'não':
            return f'O animal {self.nome} não nada'
        else:
            return f'O animal {self.nome} nada'

    def __str__(self):
        if self._predador == 'sim'.strip().upper() and self._nada == 'sim'.strip().upper():
            return f'O animal {self.nome} tem {self.peso} kilos, {self.idade} anos é um predador e nada '
        elif self._predador == 'não'.strip().upper() and self._nada == 'sim'.strip().upper():
            return f'O animal {self.nome} tem {self.peso} kilos, {self.idade} anos, ele não é um predador mas ele nada '
        elif self._predador == 'sim'.strip().upper() and self._nada == 'não'.strip().upper():
            return f'O animal {self.nome} tem {self.peso} kilos, {self.idade} anos é um predador mas ele não nada '
        elif self._predador == 'não'.strip().upper() and self._nada == 'não'.strip().upper():
            return f'O animal {self.nome} tem {self.peso} kilos,  {self.idade} anos, ele não nada e não é um predador'
        else:
            return f'Responda os dados Predador e Nadar com: SIM ou não'

Tubarao = Aquaticos('Tubarao', 30, 4, 'NÃO', 'siM' )
Cachorro = Mamifero('Cachorro', 5, 10, 0,'Marrom')

print(Cachorro)

print(Tubarao)


