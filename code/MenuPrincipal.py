from MenuCliente import *
from MenuGerente import *
from Tela import Tela
from Banco import Banco
from Gerente import Gerente
from Cliente import Cliente
from Validar import Validar

class MenuPrincipal:
    @staticmethod
    def iniciar():
        Tela.imprimir_menu_principal()
        while True:
            opcao = input('Digite o número da sua escolha: ')
            if opcao == '1':
                if Banco.existe_cliente_cadastrado():
                    Tela.limpar_console()
                    MenuPrincipal.logar_cliente()
                else:
                    Erro.lancar_erro('Não existe nenhum cliente cadastrado!')
            elif opcao == '2':
                Tela.limpar_console()
                MenuPrincipal.logar_gerente()
                break
            elif opcao == '3':
                MenuPrincipal.cadastrar_cliente()
                break
            elif opcao == '4':
                print('Programa finalizado!')
                quit()
    
    
    @staticmethod
    def logar_cliente():
        print('-----Login Cliente-----')
        while True:
            usuario = input('Digite o usuário: ')
            cliente = Banco.get_cliente_por_usuario(usuario)
            if cliente != None:
                break

        Tela.limpar_console()
        print(f'Olá {cliente.nome}!')
        while True:
            senha = input('Digite a sua senha: ')
            if cliente.verificar_senha(senha):
                Tela.limpar_console()
                Tela.imprimir_logado_como(cliente)
                MenuCliente.iniciar(cliente)
    
    
    @staticmethod
    def logar_gerente():
        print('-----Login Gerente-----')
        while True:
            senha = input('Digite a senha de gerente: ')
            if Gerente.realizar_login(senha):
                MenuGerente.iniciar()
            break
    

    @staticmethod
    def cadastrar_cliente():
        Tela.limpar_console()
        print('-----CADASTRO-----')
        nome = input('Nome do cliente: ')

        while True:
            usuario = input('Escolha um usuario: ')
            if Validar.validar_usuario(usuario):
                if Banco.usuario_disponivel(usuario):
                    break

        while True:            
            senha = input('Escolha uma senha: ')
            if Validar.validar_senha(senha):
                break

        Banco.add_cliente(Cliente(nome,usuario, senha))
        print('\033[1;32m'+f'Cliente {nome} cadastrado com sucesso! Aperte Enter para voltar ao menu principal'+'\033[0;0m')

        input()
        Tela.limpar_console()
        MenuPrincipal.iniciar()

