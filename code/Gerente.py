from Erro import Erro

class Gerente():
    nome = 'Leonardo Gerente'
    usuario = 'leo'
    senha = 'abc1234'
    
    def realizar_login(senha):
        if senha == Gerente.senha:
            return True
        else:
            Erro.lancar_erro('Senha incorreta, tente novamente')
            return False
