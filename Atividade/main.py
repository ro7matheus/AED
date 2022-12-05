from Apartamento import Apartamento
from Torre import Torre
from Fila import FilaGaragem

fila = FilaGaragem()

t1 = Torre(1, "A", "Rua A")
t2 = Torre(2, "B", "Rua B")
t3 = Torre(3, "C", "Rua C")

a1 = Apartamento(1, 100, 0, t1)
# a1.imprimir()
a2 = Apartamento(2, 200, 0, t2)
# a2.imprimir()
a3 = Apartamento(3, 300, 0, t3)
# a3.imprimir()
print("------------------------------")
print("Lista de Apartamentos e Torres")
print("------------------------------")

fila.adicionar(a1)

fila.adicionar(a3)

fila.adicionar(a2)

fila.imprimir()

fila.remover(a3, 1)

print("-----------------------------")
print("        Nova Lista           ")
print("-----------------------------")

fila.imprimir()

print("-----------------------------")
print("       Recebendo vaga        ")
print("-----------------------------")

a3.imprimir()








