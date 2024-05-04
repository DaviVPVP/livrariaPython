from model import model

class Control:
    def __init__(self):
        self.opcao = -1
        self.modelo = model()
        self.carrinho = 0

    def menu(self):
        print("Faça login para prosseguir: \n\n" +
              "0. Sair\n" +
              "1. Login\n")
        self.opcao = int(input())

    def books(self):
        print("Escolha o(s) livro(s) de sua preferência: \n\n" +
              "0. Sair \n" +
              "1. Harry Potter (R$ 30,00) \n" +
              "2. Senhor dos Anéis (R$ 40,00) \n" +
              "3. Percy Jackson (R$ 35,00) \n" +
              "4. Animal Planet (R$ 30,00) \n" +
              "5. Prosseguir com o pagamento\n ")
        self.opcao = int(input())

    def operacao(self):
        while self.opcao != 0:
            self.menu()
            if self.opcao == 0:
                print("Obrigado!")
            elif self.opcao == 1:
                self.modelo.loginSenha()
                while self.opcao != 5:
                    self.books()
                    if self.opcao == 0:
                        print("Obrigado!")
                    elif self.opcao == 1:
                        print("Harry Potter adicionado ao carrinho!")
                        self.carrinho += 30
                    elif self.opcao == 2:
                        print("Senhor dos Anéis adicionado ao carrinho!")
                        self.carrinho += 40
                    elif self.opcao == 3:
                        self.modelo.Reserva()
                    elif self.opcao == 4:
                        self.modelo.Reserva()
                    elif self.opcao == 5:
                        self.efetuarCompra()
                    else:
                        print("Escolha uma opção válida!")
            else:
                print("Código escolhido não é válido!")

    def efetuarCompra(self):
        print("Informe o cartão de crédito: ")
        dadosCartao = input()
        if self.modelo.validarCartao(dadosCartao):
            print("Compra concluída!")
        else:
            print("Erro!")



