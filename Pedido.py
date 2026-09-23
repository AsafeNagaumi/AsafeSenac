class pedido:

    status="Recebido" 

    def __init__(self, num, data, hora, cliente, itens, pag, ):
        self.num=num
        self.data=data
        self.hora=hora
        self.cliente=cliente
        self.itens=itens
        self.pagamento=pag
        

    def atualizarPedido(self, novoStatus):
        self.status=novoStatus

    def imprimir(self):
        print(f"\n|--------------- Pedido nº {self.num} -------------------------|"
              f"\n|Data: {self.data}                                       |"
              f"\n|Horário: {self.hora}                                       |"
              f"\n|Cliente: {self.cliente.nome}                                 |"
              f"\n|Itens: {self.itens}                       |"
              f"\n|Método de Pagamento: {self.pagamento}                             |"
              f"\n|Endereço: {self.cliente.endereco}                          |"
              f"\n|Telefone: {self.cliente.getTelefone()}                        |"
              f"\n|--------------------------------------------------------------|")
