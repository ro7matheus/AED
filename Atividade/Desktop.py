from Computador import Computador

class Desktop(Computador):

    def __init__(self, modelo, cor, potencia):
        super().__init__(modelo, cor, potencia)
        self.potenciaDaFonte = potencia
        print("Caracteristicas Desktop")
