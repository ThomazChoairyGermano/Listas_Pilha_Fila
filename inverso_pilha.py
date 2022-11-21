import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade  
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype = float)

    def __pilhaCheia(self):
        if self.__topo == self.__capacidade -1: 
            return True 
        else:
            return False

    def __pilhaVazia(self):
        if self.__topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):     
        if self.__pilhaCheia():
            print("A pilha está cheia")
        else:
            self.__topo += 1        
            self.__valores[self.__topo] = valor   

    def inverso(self):
        for i in self.__valores:
            if self.__topo == -1:
                print('Pilha vazia')
            else:
                pilha_invertida = self.__valores[::-1]
        return pilha_invertida

pilha = Pilha(5)
pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(55)
pilha.empilhar(45)
pilha.empilhar(52)
print(pilha.inverso())