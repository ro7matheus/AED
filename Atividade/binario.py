#Construa um algoritmo de busca contendo um vetor de números inteiros de 20 posições.
#O algoritmo deve ter duas funções, uma para busca sequencial e outra para busca binária.
#Coloque um contador em cada função para contar as iterações de cada função.
#Peça ao usuário que informe o valor que deseja procurar.
#Então informe ao usuário se este valor existe no vetor e quantas iterações foram necessárias em cada função

def pesquisa_binaria_recursiva(L, esquerda, direita, item, it=0):
    it +=1
    if direita < esquerda:
        print("Elemento {} não encontrado . Realizadas {} iterações binarias".format(item, it))
        return -1
    meio = (esquerda + direita) // 2
    if L[meio] == item:
        print("Elemento {} está na posiçõa {}. Realizadas {} iterações binarias".format(item, meio, it))
        return meio
    elif L[meio] > item:
        return pesquisa_binaria_recursiva(L, esquerda, meio - 1, item, it)
    else:
        return pesquisa_binaria_recursiva(L, meio + 1, direita, item, it)

L = [0, 10, 20, 30, 40, 50, 60, 70]

pesquisa_binaria_recursiva(L, esquerda=0, direita=len(L) - 1, item=12)