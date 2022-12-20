from binario import pesquisa_binaria_recursiva
from sequencial import pesquisa_seq

l = list(range(1, 100, 3))

print("Lista de números: ")
print(l)
item = int(input("Qual número procurar: "))
pesquisa_seq(l, item)
pesquisa_binaria_recursiva(l, esquerda=0, direita=len(l) -1, item=item)



