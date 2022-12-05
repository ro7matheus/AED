#Construa o algoritmo em Python de uma lista duplamente encadeada que possui uma função para inserir elementos em ordem alfabética, 
#uma função para imprimir os elementos da lista e uma função para imprimir os elementos na ordem inversa.

class No:
  def __init__(self, carga=None, proximo=None):
    self.carga = carga
    self.proximo = proximo

  def __str__(self):
    return str(self.carga)

def imprimeDeTrasParaFrente(lista):
  if lista == None : return
  cabeca = lista
  rabo = lista.proximo
  imprimeDeTrasParaFrente(rabo)
  print (cabeca)

def imprimeLista(no):
  while no:
    print (no)
    no = no.proximo
  print

def removeSegundo(lista):
  if lista == None : return
  primeiro = lista
  segundo = lista.proximo
  primeiro.proximo = segundo.proximo
  segundo.proximo = None
  return segundo

no1 = No("A")
no2 = No("B")
no3 = No("C")

no1.proximo = no2
no2.proximo = no3

print("Lista completa:")
imprimeLista(no1)
print("-----------------")
print("Lista inversa:")
imprimeDeTrasParaFrente(no1)
print("-----------------")
print("Item removido:")
removido = removeSegundo(no1)
imprimeLista(removido)
print("-----------------")
print("Lista atualizada:")
imprimeLista(no1)