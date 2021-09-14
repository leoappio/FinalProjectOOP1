from Erro import Erro

from Conta import Conta

class ContaPJuridica(Conta):
    def __init__(self, nome_cliente, numero_conta, saldo, cnpj, limite):
        super().__init__(nome_cliente, numero_conta, saldo)
        self.cnpj = cnpj
        self.limite = limite

    
    def pode_transferir(self, valor):
        if valor <= (self.saldo + self.limite):
            return True
        else:
            Erro.lancar_erro('Você não possui esse valor em sua conta!')
    

    def sacar(self, valor):
        if valor > 0:
            if valor <= (self.saldo + self.limite):
                self.saldo -= valor
            else:
               Erro.lancar_erro('Valor maior que o seu limite!') 
        else:
            Erro.lancar_erro('Valor de saque inválido!')
    

    def pode_sacar(self, valor):
        if valor <= (self.saldo + self.limite):
            return True
        else:
            Erro.lancar_erro('Saque ultrapassou o seu saldo!')
            return False


    def imprimir(self):
        print('Conta Pessoa Jurídica')
        print(f'Conta {self.numero_conta}')
        print(f'Cliente {self.nome_cliente}')
        print(f'Saldo: R${self.saldo:.2f}')
        print(f'CNPJ {self.cnpj}')
        print(f'Limite: R${self.limite:.2f}')
        