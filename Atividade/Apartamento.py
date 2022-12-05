from Torre import Torre

class Apartamento:

    def __init__(self, id, numeroApt, numeroVag, torre):
        self.id = id
        self.nroApt = numeroApt
        self.nroVag = numeroVag
        self.torre = torre

    def set_vagas(self, numeroVag):
        self.nroVag = numeroVag

    def imprimir(self):
        print("Número Apto:", self.nroApt)
        print("Número Vaga:", self.nroVag)
        print("Número ID Apto:", self.id)
        self.torre.imprimir()
       

