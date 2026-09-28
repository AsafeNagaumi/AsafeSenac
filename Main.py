import os
from Pedido import pedido
from Cliente import Cliente
from ItemPedido import ItemPedido
from Produto import Produto

os.system("cls")

#novoPedido = pedido(1, "14/09/26", "21:10", "João", ["X-salada", "X-Bacon"], "Pix" )
#print(novoPedido.cliente)
# print(novoPedido.status)
# #Alterar nome 67
# novoPedido.cliente="Calebe Gay"
# print(novoPedido.cliente)
# novoPedido.imprimir()
# novoPedido.atualizarPedido("Em preparação")

# print(novoPedido.atualizarPedido)
# print(novoPedido.imprimir)
ItemPedido = "5 X-Bacon"


novoCliente = Cliente(endereco="Rua Vital Brasil ",nome="João Pedro ", telefone= "+55 (67) 0178-2387 " )
novoCliente.imprimir()

novoPedido = pedido(1, "14/09/26", "21:10", novoCliente, ItemPedido, "Pix")
novoPedido.imprimir()

xbacon= Produto(cod="P01", desc="Xbacon", tipo="Lanche", valor=19.99)
xbacon.imprimirProduto()