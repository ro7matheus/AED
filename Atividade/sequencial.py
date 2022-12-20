#Construa um algoritmo de busca contendo um vetor de números inteiros de 20 posições.
#O algoritmo deve ter duas funções, uma para busca sequencial e outra para busca binária.
#Coloque um contador em cada função para contar as iterações de cada função.
#Peça ao usuário que informe o valor que deseja procurar.
#Então informe ao usuário se este valor existe no vetor e quantas iterações foram necessárias em cada função

def pesquisa_seq(l, elemento_desejado):
    it = 0
    for elemento in l:
        it +=1
        if elemento == elemento_desejado:
            print("Elementos:\n", l)
            print("Elemento {} está presente. Realizadas {} iterações sequenciais".format(elemento_desejado, it))
            return
    print("Elemento {} não está presente. Realizadas {} iterações sequenciais".format(elemento_desejado, it))

l = list(range(1, 21))

# Pesquisa por elemento presente.
pesquisa_seq(l, 10)

# Pesquisa por elemento ausente.
pesquisa_seq(l, 25)