class Torre:

    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.end = endereco

    def imprimir(self):
        print("Torre > Nome:", self.nome)
        print("Torre > Endereço:", self.end)


        