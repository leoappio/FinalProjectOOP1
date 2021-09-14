from abc import ABC, abstractmethod
from Erro import Erro

class Conta(ABC):
    def __init__(self, nome_cliente, numero_conta, saldo):
        self.nome_cliente = nome_cliente
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.movimentacoes = []
        
    def depositar(self, valor):
        self.saldo += valor
    

    def add_movimentacao(self, movimentacao):
        self.movimentacoes.append(movimentacao)
    

    def get_movimentacoes(self):
        return self.movimentacoes.copy()
    

    def detalhes(self):
        print(f' Titular: {self.nome_cliente} - Conta {self.numero_conta} - Saldo R${self.saldo:.2f}')


    def pode_transferir(self, valor):
        if valor <= self.saldo:
            return True
        else:
            Erro.lancar_erro('Você não possui esse valor em sua conta!')
            return False


    @abstractmethod
    def sacar(self, valor):
        ...


    @abstractmethod
    def imprimir(self):
        ...

    
    @abstractmethod
    def pode_sacar(self, valor):
        ...
