from Erro import Erro

class Validar:

    @staticmethod
    def validar_usuario(usuario):
        if usuario.replace(" ", "") == usuario:
            if len(usuario) > 2:
                if usuario.lower() == usuario:
                    return True
                else:
                    Erro.lancar_erro('Usuário não pode ter letras maiusculas')
                    return False
            else:
                Erro.lancar_erro('Usuário precisa ter pelo menos 3 caracteres.')
                return False
        else:
            Erro.lancar_erro('Usuário não pode conter espaços.')
            return False
    

    @staticmethod
    def validar_senha(senha):
        if senha.replace(" ", "") == senha:
            if len(senha) > 2:
                return True
            else:
                Erro.lancar_erro('A senha precisa ter pelo menos 3 caracteres.')
                return False
        else:
            Erro.lancar_erro('A senha não pode conter espaços.')
            return False
    

    @staticmethod
    def validar_numero_conta(numero):
        numeros = ['0','1','2','3','4','5','6','7','8','9']

        for caracter in numero:
            if caracter not in numeros:
                Erro.lancar_erro('Somente números são aceitos no número da conta!')
                return False
        
        return True
    

    @staticmethod
    def validar_cpf(cpf):
        numeros = ['0','1','2','3','4','5','6','7','8','9']

        for caracter in cpf:
            if caracter not in numeros:
                Erro.lancar_erro('Somente números são aceitos no CPF!')
                return False
        
        return True
    
    
    @staticmethod
    def validar_cnpj(cnpj):
        numeros = ['0','1','2','3','4','5','6','7','8','9']

        for caracter in cnpj:
            if caracter not in numeros:
                Erro.lancar_erro('Somente números são aceitos no CNPJ!')
                return False
        
        return True
    

    @staticmethod
    def validar_valor(valor):
        caracteres_permitidos = ['0','1','2','3','4','5','6','7','8','9','.']

        for caracter in valor:
            if caracter not in caracteres_permitidos:
                Erro.lancar_erro('Somente números são permitidos! (utilize ponto para números quebrados)')
                return False

        return True
    