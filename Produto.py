class Produto:

    def __init__(self, nome, valor, tipo, cod, desc):
        self.nome=nome
        self.valor=valor
        self.tipo=tipo
        self.cod=cod
        self.desc=desc


    def imprimir(self):
         print(f"\n|----------- Produto cód. {self.cod}-------------|")
         f"\n|Descrição: {self.desc}                   |"
         f"\n|Tipo: {self.tipo}                        |"
         f"\n|Preço: R$ {self.valor:.2f}               |"
         f"\n|-------------------------------------------------------|"
