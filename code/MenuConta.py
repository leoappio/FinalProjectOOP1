from Tela import Tela
from Banco import Banco
from Erro import Erro

class MenuConta:

    @staticmethod
    def iniciar(conta, cliente):
        Tela.imprimir_menu_conta()
        while True:
            opcao = input('Digite o número da sua escolha: ')
            if opcao == '1':
                MenuConta.transferencia(conta, cliente)
            elif opcao == '2':
                MenuConta.deposito(conta, cliente)
            elif opcao == '3':
                MenuConta.saque(conta, cliente)
            elif opcao == '4':
                MenuConta.imprimir_movimentacoes(conta,cliente)
                ...
            elif opcao == '5':
                Tela.limpar_console()
                Tela.imprimir_logado_como(cliente)
                from MenuCliente import MenuCliente
                MenuCliente.iniciar(cliente)

            elif opcao == '6':
                Tela.limpar_console()
                from MenuPrincipal import MenuPrincipal
                MenuPrincipal.iniciar()


    @staticmethod
    def transferencia(conta, cliente):
        Tela.limpar_console()
        Tela.imprimir_logado_como(cliente)
        Tela.imprimir_logado_conta(conta)
        contas = Banco.get_todas_contas()

        print('---------REALIZAR TRANSFERÊNCIA---------')
        Tela.imprimir_todas_contas_transferencia(contas, conta)
        print('Digite menu para voltar para o menu anterior')
        while True:
            escolha = input('Digite o número da conta que você deseja transferir: ')

            if escolha == 'menu':
                Tela.limpar_console()
                Tela.imprimir_logado_como(cliente)
                Tela.imprimir_logado_conta(conta)
                MenuConta.iniciar(conta,cliente)
            else:
                conta_destino = Banco.get_conta_por_numero(escolha)
                if conta_destino != None:
                    break
        
        while True:
            valor = float(input('Digite o valor da transferência: R$'))
            if valor > 0:
                if conta.pode_transferir(valor):
                    conta.sacar(valor)
                    conta_destino.depositar(valor)
                    break

        mov_conta = {'tipo':'Transferência Enviada', 'Conta Destino':f'{conta_destino.nome_cliente} - {conta_destino.numero_conta}','valor': valor}
        mov_conta_destino = {'tipo':'Transferência Recebida', 'Valor enviado de':f'{conta.nome_cliente} - {conta.numero_conta}','valor': valor}
        
        conta.add_movimentacao(mov_conta)
        conta_destino.add_movimentacao(mov_conta_destino)

        Tela.limpar_console()
        Tela.imprimir_logado_como(cliente)
        Tela.imprimir_logado_conta(conta)
        print('\033[1;32m'+f'Transferência realizada com sucesso! Aperte enter para voltar ao menu da conta'+'\033[0;0m')
        input()
        Tela.limpar_console()
        Tela.imprimir_logado_como(cliente)
        Tela.imprimir_logado_conta(conta)
        MenuConta.iniciar(conta, cliente)


    @staticmethod
    def deposito(conta, cliente):
        Tela.limpar_console()
        Tela.imprimir_logado_como(cliente)
        Tela.imprimir_logado_conta(conta)
        print('-----REALIZAR DEPÓSITO-----')
        while True:
            valor = float(input('Digite o valor do depósito: R$'))
            if valor > 0:
                conta.depositar(valor)
                break
            else:
                Erro.lancar_erro('Valor inválido!')

        Tela.limpar_console()
        Tela.imprimir_logado_como(cliente)
        Tela.imprimir_logado_conta(conta)
        movimentacao = {'tipo':'Deposito', 'valor': valor}
        conta.add_movimentacao(movimentacao)
        print('\033[1;32m'+f'Depósito realizado com sucesso! Aperte enter para voltar ao menu da conta'+'\033[0;0m')
        input()
        Tela.limpar_console()
        Tela.imprimir_logado_como(cliente)
        Tela.imprimir_logado_conta(conta)
        MenuConta.iniciar(conta, cliente)


    @staticmethod
    def saque(conta,cliente):
        Tela.limpar_console()
        Tela.imprimir_logado_como(cliente)
        Tela.imprimir_logado_conta(conta)
        print('-----REALIZAR SAQUE-----')

        while True:
            valor = float(input('Digite o valor do saque: R$'))

            if valor > 0 and conta.pode_sacar(valor):
                conta.sacar(valor)
                break

        Tela.limpar_console()
        Tela.imprimir_logado_como(cliente)
        Tela.imprimir_logado_conta(conta)
        movimentacao = {'tipo':'Saque', 'valor': valor}
        conta.add_movimentacao(movimentacao)
        print('\033[1;32m'+f'Saque realizado com sucesso! Aperte enter para voltar ao menu da conta'+'\033[0;0m')
        input()
        Tela.limpar_console()
        Tela.imprimir_logado_como(cliente)
        Tela.imprimir_logado_conta(conta)
        MenuConta.iniciar(conta, cliente)


    @staticmethod
    def imprimir_movimentacoes(conta, cliente):
        Tela.limpar_console()
        Tela.imprimir_logado_como(cliente)
        Tela.imprimir_logado_conta(conta)
        print()
        print('-----------MOVIMENTAÇÕES-----------')

        movimentacoes = conta.get_movimentacoes()
        Tela.imprimir_movimentacoes(movimentacoes)

        print('Aperte enter para voltar ao menu anterior')
        input()
        Tela.limpar_console()
        Tela.imprimir_logado_como(cliente)
        Tela.imprimir_logado_conta(conta)
        MenuConta.iniciar(conta, cliente)
