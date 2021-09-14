from Tela import Tela
from Erro import Erro
from Validar import Validar
from Banco import Banco
from ContaPF import ContaPFisica
from ContaPJ import ContaPJuridica
from MenuConta import MenuConta

class MenuCliente:

    @staticmethod
    def iniciar(cliente):
        Tela.imprimir_menu_cliente()
        while True:
            opcao = input('Digite o número da sua escolha: ')
            if opcao == '1':
                if cliente.ja_tem_conta_PF() == False:
                    MenuCliente.criar_conta_pessoa_fisica(cliente)
                else:
                    Erro.lancar_erro('Você já tem uma conta pessoa física!')
            elif opcao == '2':
                MenuCliente.criar_conta_pessoa_juridica(cliente)
            elif opcao == '3':
                Tela.imprimir_contas_cliente(cliente)
                input()
                Tela.limpar_console()
                Tela.imprimir_logado_como(cliente)
                MenuCliente.iniciar(cliente)
            elif opcao == '4':
                MenuCliente.entrar_em_uma_conta(cliente)
            elif opcao == '5':
                MenuCliente.trocar_senha(cliente)
            elif opcao == '6':
                Tela.limpar_console()
                from MenuPrincipal import MenuPrincipal
                MenuPrincipal.iniciar()


    @staticmethod
    def criar_conta_pessoa_fisica(cliente):
        Tela.limpar_console()
        print('-----Criar Conta pessoa Física-----')
        while True:
            numero_conta = input('Escolha um número para a conta:')
            if Validar.validar_numero_conta(numero_conta):
                if Banco.numero_conta_disponivel(numero_conta):
                    break
        
        while True:
            saldo = input('Saldo inicial da conta: R$')
            if Validar.validar_valor(saldo):
                saldo = float(saldo)
                if saldo >= 0:
                    break
        
        while True:
            cpf = input('Digite o CPF: ')
            if Validar.validar_cpf(cpf):
                break
        
        nova_conta = ContaPFisica(cliente.nome, numero_conta, saldo, cpf)
        cliente.add_conta(nova_conta)
        Banco.add_conta(nova_conta)

        movimentacao = {'tipo':'Deposito Inicial', 'valor': saldo}
        nova_conta.add_movimentacao(movimentacao)
        print('\033[1;32m'+f'Conta {numero_conta} foi criada com sucesso! Aperte Enter para voltar ao menu do cliente'+'\033[0;0m')

        input()
        Tela.limpar_console()
        Tela.imprimir_logado_como(cliente)
        MenuCliente.iniciar(cliente)


    @staticmethod
    def criar_conta_pessoa_juridica(cliente):
        Tela.limpar_console()
        print('-----Criar Conta Pessoa Jurídica-----')
        while True:
            numero_conta = input('Escolha um número para a conta:')
            if Validar.validar_numero_conta(numero_conta):
                if Banco.numero_conta_disponivel(numero_conta):
                    break
        
        while True:
            saldo = input('Saldo inicial da conta: R$')
            if Validar.validar_valor(saldo):
                saldo = float(saldo)
                if saldo >= 0:
                    break
            else:
                Erro.lancar_erro('Saldo não pode ser negativo')
        
        while True:
            cnpj = input('Digite o CNPJ: ')
            if Validar.validar_cnpj(cnpj):
                break
        
        while True:
            limite = input('Digite o limite para essa conta: R$')
            if Validar.validar_valor(limite):
                limite = float(limite)
                if limite >= 0:
                    break
            else:
                Erro.lancar_erro('Limite não pode ser negativo')
        
        nova_conta = ContaPJuridica(cliente.nome, numero_conta, saldo, cnpj, limite)
        cliente.add_conta(nova_conta)
        movimentacao = {'tipo':'Deposito Inicial', 'valor': saldo}
        nova_conta.add_movimentacao(movimentacao)
        Banco.add_conta(nova_conta)
        print('\033[1;32m'+f'Conta {numero_conta} foi criada com sucesso! Aperte Enter para voltar ao menu do cliente'+'\033[0;0m')

        input()
        Tela.limpar_console()
        Tela.imprimir_logado_como(cliente)
        MenuCliente.iniciar(cliente)


    @staticmethod
    def entrar_em_uma_conta(cliente):
        Tela.limpar_console()
        Tela.imprimir_logado_como(cliente)
        print('-----ESCOLHA UMA CONTA-----')
        contas = cliente.get_contas()

        print('[0] - Voltar ao menu anterior')
        for indice,conta in enumerate(contas):
            if type(conta) == ContaPFisica:
                print(f'[{indice+1}] PF - Número: {conta.numero_conta} - Saldo: R${conta.saldo:.2f}')
            else:
                print(f'[{indice+1}] PJ - Número: {conta.numero_conta} - Saldo: R${conta.saldo:.2f}')

        
        while True:
            escolha = int(input('Digite o número da conta para entrar: '))
            if 0 < escolha <= len(contas):
                break
            elif escolha == 0:
                Tela.limpar_console()
                Tela.imprimir_logado_como(cliente)
                MenuCliente.iniciar(cliente)
            else:
                Erro.lancar_erro('Número inválido!')
        
        conta_selecionada = contas[escolha-1]

        Tela.limpar_console()
        Tela.imprimir_logado_como(cliente)
        Tela.imprimir_logado_conta(conta_selecionada)
        MenuConta.iniciar(conta_selecionada, cliente)


    @staticmethod
    def trocar_senha(cliente):
        Tela.limpar_console()
        print('-----Trocar Senha-----')
        while True:
            senha_atual = input('digite a sua senha atual: ')
            if cliente.verificar_senha(senha_atual):
                break

        while True:
            senha_nova = input('Digite a nova senha: ')
            if Validar.validar_senha(senha_nova):
                break
        
        cliente.alterar_senha(senha_nova)
        print('\033[1;32m'+f'Senha alterada com sucesso! Aperte enter para voltar ao menu de cliente'+'\033[0;0m')

        input()
        Tela.limpar_console()
        Tela.imprimir_logado_como(cliente)
        MenuCliente.iniciar(cliente)