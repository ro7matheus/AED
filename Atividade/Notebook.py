from Computador import Computador

class Notebook(Computador):

    def __init__(self, modelo, cor, tempo):
        super().__init__(modelo, cor, tempo)
        self.tempoDeBateria = tempo
        print("Caracteristicas Notebook")
