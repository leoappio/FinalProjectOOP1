class Erro:

    @staticmethod
    def lancar_erro(erro):
        cor_vermelho = '\033[31m'
        cor_branco = '\033[0;0m'

        print(cor_vermelho + erro + cor_branco)
