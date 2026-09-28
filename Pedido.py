class pedido:

    status="Recebido" 

    def __init__(self, num, data, hora, cliente, itens, pag, produtos, tipo, valor, Valortotal ):
        self.num=num
        self.data=data
        self.hora=hora
        self.cliente=cliente
        self.itemPedido=itens
        self.pagamento=pag
        self.produtos=produtos
        self.tipo=tipo
        self.valor=valor
        self.Valortotal=Valortotal
        

    def atualizarPedido(self, novoStatus):
        self.status=novoStatus

    def imprimir(self):
        print(f"\n|--------- Pedido nº {self.num} ----------|"
              f"\n|Data: {self.data}                  |"
              f"\n|Horário: {self.hora}                  |"
              f"\n|Cliente: {self.cliente.nome}            |"
              f"\n|Itens: {self.itemPedido}                |"
              f"\n|Método de Pagamento: {self.pagamento}        |"
              f"\n|Endereço: {self.cliente.endereco}     |"
              f"\n|Telefone: {self.cliente.getTelefone()}   |"
              f"\n|Tipo: {self.tipo}        |"
              f"\n|Produtos: {self.produtos}({self.valor})      |"
              f"\n|Valor Total: {self.Valortotal}            |"                          
              f"\n|--------------------------------|")
