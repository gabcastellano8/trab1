from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria
        
    def getInformacoes(self):
        print("Modelo: ", self.modelo)
        print("Cor: ", self.cor)
        print("Preço: ", self.preco)
        print("Tempo de Bateria: ", self.__tempoDeBateria)
    
    def cadastrar(self):
        print("Cadastro de Notebook realizado com sucesso!")