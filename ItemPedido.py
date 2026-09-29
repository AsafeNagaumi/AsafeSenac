class ItemPedido:

    def __init__(self, produto, obs, qtd, desconto):
        self.produto = produto
        self.observacao = obs
        self.quantidade = qtd
        self.desconto = desconto

    def TotalItem(self):
        valor = (self.quantidade * self.produto.preco) - self.desconto
        return valor
