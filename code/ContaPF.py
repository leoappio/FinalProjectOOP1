from Erro import Erro
from Conta import Conta

class ContaPFisica(Conta):
    def __init__(self, nome_cliente, numero_conta, saldo, cpf):
        super().__init__(nome_cliente, numero_conta, saldo)
        self.cpf = cpf
    

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
            else:
                Erro.lancar_erro('Valor maior que o seu saldo!')
        else:
            Erro.lancar_erro('Valor de saque inválido!')
    

    def pode_sacar(self, valor):
        if valor <= self.saldo:
            return True
        else:
            Erro.lancar_erro('Saque ultrapassou o seu saldo!')
            return False


    def imprimir(self):
        print('Conta Pessoa Física')
        print(f'Conta {self.numero_conta}')
        print(f'Cliente {self.nome_cliente}')
        print(f'Saldo: R${self.saldo:.2f}')
        print(f'CPF {self.cpf}')
                