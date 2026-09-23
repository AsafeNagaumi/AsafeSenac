import os
from Pedido import pedido
from Cliente import Cliente

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


novoCliente = Cliente(endereco="Rua Vital Brasil ",nome="Menino gay ", telefone= "67 (+55) 0178-2387 ")
novoCliente.imprimir()

novoPedido = pedido(1, "14/09/26", "21:10", novoCliente, 
                     ["X-salada", "X-Bacon"], "Pix",  )
novoPedido.imprimir()