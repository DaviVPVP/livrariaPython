class model:
    def __init__(self):
        self.login = ""
        self.senha = ""
        self.nome = ""
        self.endereco = ""
        self.telefone = ""
        self.nascimento = ""
        self.resposta = -1
        self.contato = ""
        self.opcao = -1
        self.i = 0

    def loginSenha(self):
        print("Você já possui cadastro? \n1. Sim\n2. Não")
        self.resposta = int(input())
        if self.resposta == 1:
            print("Informe seu login: ")
            self.login = input()
            print("Informe sua senha: ")
            self.senha = input()
        else:
            print("Informe seu nome: ")
            self.nome = input()
            print("Informe seu endereço: ")
            self.endereco = input()
            print("Informe seu telefone: ")
            self.telefone = input()
            print("Informe sua data de nascimento: ")
            self.nascimento = input()
            print("Informe seu login: ")
            self.login = input()
            print("Informe sua senha: ")
            self.senha = input()
            print("CADASTRO CONCLUÍDO!")

            print("Informe seu login: ")
            while input() != self.login:
                print("Usuário não identificado! \n"
                      "Informe seu login: ")

            print("Informe sua senha: ")
            while input() != self.senha:
                print("Senha incorreta! \n"
                      "Informe sua senha: ")

            print("Seja Bem vindo(a)!")

    def Reserva(self):
        print("Livro indisponível ): Gostaria de fazer a reserva do livro? \n" +
              "1. Sim \n" +
              "2. Não \n")
        self.opcao = int(input())

        if self.opcao == 1:
            print("Informe seu e-mail ou número de telefone: ")
            self.contato = input()
            print("Você será notificado(a) quando este livro ou livros estiverem disponíveis! \n")

    def validarCartao(self, dadosCartao):
        self.i = 0
        for i in dadosCartao:
            i += 1
            if i > 8:
                print("Erro!")





