from Banco import Banco
from ContaPF import ContaPFisica
import os

class Tela:
    @staticmethod
    def limpar_console():
        os.system('cls' if os.name == 'nt' else 'clear')


    @staticmethod
    def imprimir_menu_principal():
        print('----------Menu Principal----------')
        print('[1] - Logar como Cliente')
        print('[2] - Logar como Gerente')
        print('[3] - Criar nova conta como cliente')
        print('[4] - Finalizar Programa')


    @staticmethod
    def imprimir_menu_cliente():
        print('----------Menu Cliente----------')
        print('[1] - Criar Conta Pessoa Física')
        print('[2] - Criar Conta Pessoa Jurídica')
        print('[3] - Listar todas as minhas contas')
        print('[4] - Entrar em uma conta')
        print('[5] - Trocar minha senha')
        print('[6] - Voltar ao menu principal')


    @staticmethod
    def imprimir_menu_conta():
        print('----------Menu Conta----------')
        print('[1] - Realizar uma transferência')
        print('[2] - Realizar um deposito')
        print('[3] - Realizar um saque')
        print('[4] - Ver movimentações da minha conta')
        print('[5] - voltar ao menu de cliente')
        print('[6] - voltar ao menu principal')


    @staticmethod
    def imprimir_menu_gerente():
        print('----------Menu Gerente----------')
        print('[1] - Imprimir todas as contas cadastradas no Banco')
        print('[2] - Imprimir todos os clientes cadastrados no Banco')
        print('[3] - Apagar uma conta')
        print('[4] - Apagar um cliente')
        print('[5] - voltar ao menu principal')


    @staticmethod
    def imprimir_logado_como(cliente):
        verde = '\033[1;32m'
        branco = '\033[0;0m'
        print(verde+f'Logado como: {cliente.nome}'+branco)


    @staticmethod
    def imprimir_logado_conta(conta):
        verde = '\033[1;32m'
        branco = '\033[0;0m'

        if type(conta) == ContaPFisica:
            print(verde+f'PF - Conta: {conta.numero_conta} - Saldo: R${conta.saldo:.2f}'+branco)
        else:
            print(verde+f'PJ - Conta: {conta.numero_conta} - Saldo: R${conta.saldo:.2f} - Limite: R${conta.limite:.2f}'+branco)

    
    @staticmethod
    def imprimir_contas_cliente(cliente):
        Tela.limpar_console()
        print('---------SUAS CONTAS---------')
        contas = cliente.get_contas()

        for conta in contas:
            print('-'*29)
            conta.imprimir()
        
        print('-'*29)
        print('Aperte enter para voltar ao menu de cliente')
    

    @staticmethod
    def imprimir_todas_contas_transferencia(contas, conta_para_nao_imprimir):
        for conta in contas:
            if conta != conta_para_nao_imprimir:
                print('-'*40)
                print(f'Titular: {conta.nome_cliente} - Número da conta: {conta.numero_conta}')
        
        print('-'*40)


    @staticmethod
    def imprimir_todas_contas(contas):
        for conta in contas:
            print('-'*45)
            print(f'Titular: {conta.nome_cliente} - Número da conta: {conta.numero_conta}')
        
        print('-'*45)
    

    @staticmethod
    def imprimir_todas_contas_banco():
        contas = Banco.get_todas_contas()
        for conta in contas:
            print('-'*60)
            if type(conta) == ContaPFisica:
                print(f'PF - Titular: {conta.nome_cliente} - CPF: {conta.cpf} - Número da conta: {conta.numero_conta} - Saldo: R${conta.saldo:.2f}')
            else:
                print(f'PJ - Titular: {conta.nome_cliente} - CNPJ: {conta.cnpj} - Número da conta: {conta.numero_conta} - Saldo: R${conta.saldo:.2f} - Limite: R${conta.limite:.2f}')

        print('-'*60)
        print('Aperte enter para voltar ao menu de gerente')
    

    @staticmethod
    def imprimir_todos_os_clientes():
        clientes = Banco.get_todos_clientes()
        for cliente in clientes:
            print('-'*40)
            print(f'Nome: {cliente.nome} - Usuario: {cliente.usuario} - Quantidade de contas: {cliente.get_quantidade_de_contas()}')
        print('-'*40)
    

    @staticmethod
    def imprimir_movimentacoes(movimentacoes):
        for movimentacao in movimentacoes:
            print('-'*35)
            if movimentacao['tipo'] == 'Transferência Enviada':
                print(f'Transferência Enviada')
                print('Conta Destino:',movimentacao['Conta Destino'])
                print('Valor Enviado R$',movimentacao['valor'])

            elif movimentacao['tipo'] == 'Transferência Recebida':
                print(f'Transferência Recebida')
                print('Valor recebido de',movimentacao['Valor enviado de'])
                print('Valor Recebido R$',movimentacao['valor'])
            
            else:
                print(movimentacao['tipo'])
                print('Valor R$',movimentacao['valor'])

        print('-'*35)
