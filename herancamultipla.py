class Empresa:
    def oi(self):
        print('Oi Empresa')
class Hospital(Empresa):
    def oi(self):
        print('Oi, Hospital')

class Laboratorio(Empresa):
    def imprimirRelatorio(self):
        print('Relatorio Laboratorial')

    def tchau(self):
        print('Tchau Laboratorial')


class Junior(Hospital):
    pass

class Pleno(Laboratorio):
    pass


class Senior(Hospital, Laboratorio):
    pass


Tassio = Senior()

Tassio.oi()
Tassio.tchau()
