from Computador import Computador
       
class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self.__potenciaDaFonte = potenciaDaFonte
    
    def getInformacoes(self):
        print("Modelo: ", self.modelo)
        print("Cor: ", self.cor)
        print("Preço: ", self.preco)
        print("Potência da Fonte: ", self.__potenciaDaFonte)
       
    def cadastrar(self):
        print("Cadastro de Desktop realizado com sucesso!")