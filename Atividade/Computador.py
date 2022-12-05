from abc import ABCMeta, abstractmethod
#from pyexpat import  modelo

class Computador(metaclass=ABCMeta):

    def __init__(self, modelo, cor, preco):
        self.__modelo = modelo
        self._cor = cor
        self.preco = preco
        print("PC montado")

    def imprimir(self):
        print("Modelo: ", self.__modelo)
        print("Cor: ", self._cor)

    #@abstractmethod
    #def Cadastrar(self):
    #    pass

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, valor):
        self.__modelo(valor)

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor

    #@abstractmethod
    #def Cadastrar(self):
    #    pass
    #    self.modelo.append(modelo)
    #    self.cor.append(cor)
    #    self.preco.append(preco)

