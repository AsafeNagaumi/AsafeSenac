class Pedido:
    status = "Recebido"

    def __init__(self, num, data, hora, cliente, itens, pagamento):
        self.num = num
        self.data = data
        self.hora = hora
        self.cliente = cliente
        self.itens = itens   
        self.pagamento = pagamento

    def atualizarPedido(self, novoStatus):
        self.status = novoStatus

    def imprimir(self):
        print(f"\n--------- Pedido nº {self.num} --------------|"
              f"\nData: {self.data}                      |"
              f"\nHorário: {self.hora}                      |"
              f"\nCliente: {self.cliente.nome}                       |"
              f"\nMétodo de Pagamento: {self.pagamento}            |"
              f"\nEndereço: {self.cliente.endereco}             |"
              f"\nTelefone: {self.cliente.getTelefone()}        |"
              f"\nStatus: {self.status}                    |")

        for item in self.itens:
            print(f"------------------------------------|\n"
                  f"Produto: {item.produto.descricao} "
                  f"- Qtd: {item.quantidade}| \n- Valor: {item.produto.preco}       "
                  f"- Total: {item.TotalItem()}  |"
                  f"\n------------------------------------|")