class Cliente:
 
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.__telefone = telefone
        self.endereco = endereco

    def getTelefone(self):
        return self.__telefone

    def setTelefone(self, telefone):
        self.__telefone=telefone
 
        # Métodos - ações
 
    def imprimir(self):
        print(f"|--Nome: {self.nome}---|")
        print(f"|--Telefone: {self.__telefone}--|")
        print(f"|--Endereço: {self.endereco}--|")
 

        
 