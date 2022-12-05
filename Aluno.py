class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    
    def imprimir(self):
        # print("Código: "+ self.codigo)
        # print("Nome: "+ self.nome)
        # print("Matricula: "+ self.matricula)

        print(f"Aluno {self.nome}: Código {self.codigo}, Matricula: {self.matricula}")

# if __name__ == "__main__":    
#     a = Aluno("1", "Matheus", "123456")
#     print(a.nome)





