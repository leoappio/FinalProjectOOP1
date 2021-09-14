from Erro import Erro
from ContaPF import ContaPFisica
from ContaPJ import ContaPJuridica

class Cliente():
    def __init__(self, nome, usuario, senha):
        self.nome = nome
        self.usuario = usuario
        self.senha = senha
        self.contas = []
    

    def add_conta(self, conta):
        self.contas.append(conta)
    
    def remover_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                self.contas.remove(conta)

    def get_quantidade_de_contas(self):
        return len(self.contas)

    
    def ja_tem_conta_PF(self):
        for conta in self.contas:
            if type(conta) == ContaPFisica:
                return True
        
        return False

    def verificar_senha(self, senha):
        if self.senha == senha:
            return True
        
        Erro.lancar_erro('Senha Inválida, tente novamente!')
        return False
    
    def get_contas(self):
        return self.contas.copy()

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha
    

            