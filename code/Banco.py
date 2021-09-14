from Gerente import Gerente
from Erro import Erro

class Banco:

    clientes = []
    contas = []
    gerente = Gerente()
   

    @staticmethod
    def add_cliente(cliente):
        Banco.clientes.append(cliente)


    @staticmethod
    def add_conta(conta):
        Banco.contas.append(conta)


    @staticmethod
    def numero_conta_disponivel(numero):
        for conta in Banco.contas:
            if conta.numero_conta == numero:
                Erro.lancar_erro('Número de conta já está em uso, tente outro')
                return False
        
        return True


    @staticmethod
    def usuario_disponivel(usuario_para_verificar):
        for cliente in Banco.clientes:
            if cliente.usuario == usuario_para_verificar:
                Erro.lancar_erro('Usuário já está em uso, escolha outro')
                return False
        
        return True


    @staticmethod
    def remover_conta(nro_conta_para_remover):
        for conta in Banco.contas:
            if conta.numero_conta == nro_conta_para_remover:
                cliente = Banco.get_cliente_por_conta(nro_conta_para_remover)
                cliente.remover_conta(nro_conta_para_remover)
                Banco.contas.remove(conta)
                break
    

    @staticmethod
    def remover_cliente(cliente_para_remover):
        for cliente in Banco.clientes:
            if cliente == cliente_para_remover:
                Banco.clientes.remove(cliente)
                break


    @staticmethod
    def get_cliente_por_usuario(usuario):
        for cliente in Banco.clientes:
            if cliente.usuario == usuario:
                return cliente

        Erro.lancar_erro('Não existe cliente com esse usuário')
        return None


    @staticmethod
    def get_cliente_por_conta(numero_conta):
        for conta in Banco.contas:
            if conta.numero_conta == numero_conta:
                for cliente in Banco.clientes:
                    if conta.nome_cliente == cliente.nome:
                        return cliente    


    @staticmethod
    def get_todas_contas():
        return Banco.contas.copy()  


    @staticmethod
    def get_todos_clientes():
        return Banco.clientes.copy()


    @staticmethod
    def get_conta_por_numero(numero):
        for conta in Banco.contas:
            if conta.numero_conta == numero:
                return conta

        Erro.lancar_erro('Não existe nenhuma conta com esse número!')
        return None
    

    @staticmethod
    def existe_cliente_cadastrado():
        if len(Banco.clientes) > 0:
            return True
        
        return False
        