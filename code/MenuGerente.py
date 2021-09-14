from Tela import Tela
from Gerente import Gerente
from Banco import Banco


class MenuGerente:
    
    @staticmethod
    def iniciar():
        Tela.limpar_console()
        Tela.imprimir_logado_como(Gerente)
        Tela.imprimir_menu_gerente()
        while True:
            opcao = input('Digite o número da sua escolha: ')
            if opcao == '1':
                Tela.limpar_console()
                Tela.imprimir_todas_contas_banco()
                input()
                MenuGerente.iniciar()
            elif opcao == '2':
                Tela.limpar_console()
                Tela.imprimir_todos_os_clientes()
                print('Aperte enter para voltar ao menu de gerente')
                input()
                MenuGerente.iniciar()
            elif opcao == '3':
                MenuGerente.apagar_conta()
            elif opcao == '4':
                MenuGerente.apagar_cliente()
            elif opcao == '5':
                Tela.limpar_console()
                from MenuPrincipal import MenuPrincipal
                MenuPrincipal.iniciar()


    @staticmethod
    def apagar_conta():
        Tela.limpar_console()
        print('-----APAGAR CONTA-----')
        Tela.imprimir_todas_contas(Banco.get_todas_contas())

        while True:
            conta_para_apagar = input('Digite o número da conta que quer apagar: ')
            if Banco.get_conta_por_numero(conta_para_apagar) != None:
                break
        
        Banco.remover_conta(conta_para_apagar)
        print('\033[1;32m'+f'Conta apagada com sucesso! Aperte enter para voltar ao menu de gerente'+'\033[0;0m')
        input()
        MenuGerente.iniciar()


    @staticmethod
    def apagar_cliente():
        Tela.limpar_console()
        print('-----APAGAR CLIENTE-----')
        Tela.imprimir_todos_os_clientes()

        while True:
            cliente_para_apagar = input('Digite o usuário do cliente que quer apagar: ')
            cliente = Banco.get_cliente_por_usuario(cliente_para_apagar)
            if cliente != None:
                break
        
        contas_cliente = cliente.get_contas()

        for conta in contas_cliente:
            Banco.remover_conta(conta.numero_conta)
        
        Banco.remover_cliente(cliente)
        print('\033[1;32m'+f'Cliente apagado com sucesso! Aperte enter para voltar ao menu de gerente'+'\033[0;0m')
        input()
        MenuGerente.iniciar()