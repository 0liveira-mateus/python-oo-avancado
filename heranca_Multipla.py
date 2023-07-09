class Pai:
    def __init__(self, Nome, sobrenome_pai):
        self.__Nome = Nome
        self.__sobrenome_pai = sobrenome_pai
    @property
    def Nome(self):
        return self.__Nome

    @property
    def sobrenome_pai(self):
        return self.__sobrenome_pai

class Mae:
    def __init__(self, Nome, sobrenome_Mae):
        self.__nome = Nome
        self.__sobrenome_Mae = sobrenome_Mae

    @property
    def sobrenome_Mae(self):
        return self.__sobrenome_Mae


class Filho(Pai, Mae):
    def __init__(self, Nome, sobrenome_pai, sobrenome_Mae):
        Pai.__init__(self, Nome, sobrenome_pai)
        Mae.__init__(self, 0, sobrenome_Mae)

    def __str__(self):
        return f'{self.Nome} herdou de seu pai o sobrenome {self.sobrenome_pai} e {self.sobrenome_Mae} de sua mãe'

Mateus = Filho('Mateus', 'Marques', 'Santos')

print(Mateus.sobrenome_pai)
print(Mateus.sobrenome_Mae)