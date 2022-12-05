from Apartamento import Apartamento

class FilaGaragem:

    def __init__(self):
        self.fila = []

    def adicionar(self, ap):
        self.fila.append(ap)

    def remover(self, ap, qtdVagas):
        ap.set_vagas(qtdVagas)
        self.fila.remove(ap)

    def imprimir(self):
        for ap in self.fila:
            ap.imprimir()





